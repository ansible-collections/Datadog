import yaml
from yaml.loader import SafeLoader
import json
from invoke import task
import re

DESCRIPTION_REGEX = "\(([a-zA-Z\._]+)\)"
REPLACEMENT_REGEX = "`([a-zA-Z\._]+)`"
WIN_REGEX = "`([a-zA-Z\._]+)`"


class SafeLineLoader(SafeLoader):
    """
    Extend yaml SafeLoader to add the '__line__' key when loading a yaml file.
    """

    def construct_mapping(self, node, deep=False):
        mapping = super(SafeLineLoader, self).construct_mapping(node, deep=deep)
        mapping["__line__"] = node.start_mark.line + 1
        return mapping


def generate_fqcn_format_map(ctx):
    """
    Parse the ansible-lint output on fqcn errors only to create a hashmap on all changes that needs to be done per file.
    """
    output = ctx.run("ansible-lint -t fqcn -x yaml -f json -q || true", hide=True)
    fqcn_data = json.loads(output.stdout)
    if not fqcn_data:
        return {}
    fqcn_format_hash = {}
    for fqcn_error in fqcn_data:
        try:
            file_path = fqcn_error["location"]["path"]
            task_line_nb = fqcn_error["location"]["lines"]["begin"]
            replacement = re.search(REPLACEMENT_REGEX, fqcn_error["content"]["body"])
            action = re.search(DESCRIPTION_REGEX, fqcn_error["description"])
        except KeyError as e:
            print("[WARN] failed to parse the following with key : ", e)
            print(fqcn_error)
            continue
        if not replacement or not action:
            replacement = re.search(WIN_REGEX, fqcn_error["description"])
            action = re.search(WIN_REGEX, fqcn_error["content"]["body"])
            if not replacement and not action:
                print(
                    "[ERROR] format_fqcn: can't find the replacement necessary... SKIPPING"
                )
                print(fqcn_error)
                continue

        replacement = replacement.group(1)
        action = action.group(1)
        if fqcn_format_hash.get(file_path, None) is None:
            fqcn_format_hash[file_path] = set()
        fqcn_format_hash[file_path].add((task_line_nb, replacement, action))

    return fqcn_format_hash


def get_yaml_line_index(yaml_content, line_nb):
    """
    Return a list of rule index for a specific line in the file.

    Example:
    - block:
        - name: "Sample rule"

    Rule line 1 is contained inside the block rule line 0.
    get_yaml_line_index(yaml_content, 1) -> [0 , 1]
    """
    for k, rules in enumerate(yaml_content):
        if rules["__line__"] == line_nb:
            return [k]
        if rules.get("block", None) is not None:
            result = get_yaml_line_index(rules["block"], line_nb)
            if result is not None:
                return [k] + result
    return None


def delete_yaml_key(yaml_content, key):
    """
    Delete all 'key' from a loaded yaml.
    """
    if type(yaml_content) is dict:
        if key in yaml_content:
            yaml_content.pop(key)
        for value in yaml_content.values():
            delete_yaml_key(value, key)
    elif type(yaml_content) is list:
        for value in yaml_content:
            delete_yaml_key(value, key)


@task
def format_fqcn(ctx):
    """
    Format all fqcn ansible-lint errors.
    """
    fqcn_format_hash = generate_fqcn_format_map(ctx)
    for file in fqcn_format_hash.keys():
        with open(file, "r") as fd:
            yaml_content = yaml.load(fd.read(), Loader=SafeLineLoader)
        for line_nb, missing_prefix, action in fqcn_format_hash[file]:
            yaml_indexes = get_yaml_line_index(yaml_content, line_nb)
            if yaml_indexes is None:
                raise Exception(
                    f"Invalid line number : {line_nb}\nDoesn't correspond to any rule."
                )

            cur_yaml_content = yaml_content
            for index in yaml_indexes:
                if type(cur_yaml_content) is dict:
                    cur_yaml_content = cur_yaml_content["block"]
                cur_yaml_content = cur_yaml_content[index]
            for key in cur_yaml_content.copy():
                if key == action:
                    cur_yaml_content[missing_prefix] = cur_yaml_content.pop(action)

        delete_yaml_key(yaml_content, "__line__")
        with open(file, "w") as fd:
            yaml.dump(yaml_content, fd, sort_keys=False)

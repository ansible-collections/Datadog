from __future__ import absolute_import, division, print_function
import json
from invoke import task
import re

__metaclass__ = type


DESCRIPTION_REGEX = r"\(([a-zA-Z\._]+)\)"
REPLACEMENT_REGEX = r"`([a-zA-Z\._]+)`"
WIN_REGEX = r"`([a-zA-Z\._]+)`"


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
        fqcn_format_hash[file_path].add((replacement, action))

    return fqcn_format_hash


@task
def format_fqcn(ctx):
    """
    Format all fqcn ansible-lint errors.
    """
    fqcn_format_hash = generate_fqcn_format_map(ctx)
    for file in fqcn_format_hash.keys():
        fd = open(file, "r+")
        content = fd.read()
        for replacement, action in fqcn_format_hash[file]:
            content = re.sub(f"^([ \t]+){action}:", r"\1" + replacement + ":", content)

        fd.seek(0)
        fd.write(content)
        fd.truncate()
        fd.close()

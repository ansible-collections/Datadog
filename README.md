# Datadog ansible collection

## Description

The Datadog Ansible collection, `datadog.dd`, is the official collection of Ansible-related Datadog content. At the moment, it only contains the [Ansible Datadog Role](https://github.com/DataDog/ansible-datadog/). This role can be accessed as `datadog.dd.agent`, allowing to install and configure the Datadog Agent and integrations. Agent version 7 is installed by default.

## Requirements

- Requires Ansible v2.10+.
- Supports most Debian, RHEL-based and SUSE-based Linux distributions, macOS, and Windows.
- When using to manage Windows hosts, requires the `ansible.windows` collection to be installed:

  ```shell
  ansible-galaxy collection install ansible.windows
  ```
- When using to manage openSUSE/SLES hosts, requires the `community.general` collection to be installed:
  
  ```shell
  ansible-galaxy collection install community.general
  ```

## Installation

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install datadog.dd
```

You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:


```yaml
collections:
  - name: datadog.dd
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the Ansible package. 
To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install datadog.dd --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 5.0.0:

```
ansible-galaxy collection install datadog.dd:==5.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

The Datadog Ansible collection is also available through the [Red Hat Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/datadog/dd/), where it is officially certified by Red Hat.

## Use Cases

To deploy the Datadog Agent on hosts, add the Datadog role and your API key to your playbook:

```yaml
- hosts: servers
  tasks:
    - name: Import the Datadog Agent role from the Datadog collection
      import_role:
        name: datadog.dd.agent
  vars:
    datadog_api_key: "<YOUR_DD_API_KEY>"
```

Note for users installing the collection through the Ansible Automation Hub: OpenSUSE/SLES functionality depends on a community collection `community.general`. Red Hat Support does not provide support for any issues related to community content. Thus, all support issues for OpenSUSE/SLES should be directed to Datadog Support.


## Testing

Collection tested on centos, debian, rocky linux, opensuse, windows and macOS. Running with latest ansible-lint version and sanity checks running with python 3.9 to python 3.12.

## Support

If you need support, you can create in issue or open a support ticket to datadog directly.

## Release Notes

You can follow changes in our [CHANGELOG](https://github.com/ansible-collections/Datadog/blob/main/CHANGELOG.rst) file

## Related Information

### Collection role list

- `datadog.dd.agent`: Installation and configuration of the Datadog Agent.
  - See [the official documentation for the role](https://docs.datadoghq.com/agent/guide/ansible_standalone_role/#setup).
  - See [the repository for the standalone role](https://github.com/DataDog/ansible-datadog#readme).

## License Information

This repository is under [Apache License 2.0](https://github.com/ansible-collections/Datadog/blob/main/LICENSE).

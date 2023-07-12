# Datadog Collection

This repository contains the ``datadog.dd`` Ansible Collection. This collection only contains the Ansible Datadog Role at the moment.
This role can be access through ``datadog.dd.agent`` allowing to install and configure the Datadog Agent and integrations. By default the agent v7 is installed.

## Setup

### Requirements

- Requires Ansible v2.10+.
- Supports most Debian and RHEL-based Linux distributions, macOS, and Windows.
- When using to manage Windows hosts, requires the `ansible.windows` collection to be installed:

  ```shell
  ansible-galaxy collection install ansible.windows
  ```
- When using to manage openSUSE/SLES hosts, requires the `community.general` collection to be installed:
  
  ```shell
  ansible-galaxy collection install community.general
  ```

### Installation

NOTE: the collection hasn't been released as of now, the below instructions will apply as soon as it gets released.

```shell
ansible-galaxy collection install datadog.dd
```

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

Note for users installing the collection through the Ansible Automation Hub: OpenSUSE/SLES functionality depends on a community collection community.general. Red Hat Support does not provide support for any issues related to community content. Thus, all support issues for OpenSUSE/SLES should be directed to Datadog Support.

### Collection role list
  - ``datadog.dd.agent`` : Installation and configuration of the Datadog agent ([full documentation](https://github.com/DataDog/ansible-datadog/blob/main/README.md))

# Datadog Collection

This repository contains the ``datadog.dd`` Ansible Collection. This collection only contains the Ansible Datadog Role at the moment.
This role can be access through ``datadog.dd.agent`` allowing to install and configure the Datadog Agent and integrations. By default the agent v7 is installed.

## Setup

### Requirements

- Requires Ansible v2.6+.
- Supports most Debian and RHEL-based Linux distributions, macOS, and Windows.
- When using Ansible 2.10+ on Windows, requires the `ansible.windows` collection to be installed:

  ```shell
  ansible-galaxy collection install ansible.windows
  ```

### Installation

(Collection not available at the moment)

```shell
ansible-galaxy collection install datadog.dd
```

### Collection role list
  - ``datadog.dd.agent`` : Instllation and configuration of the Datadog agent ([full documentation](https://github.com/DataDog/ansible-datadog/blob/main/README.md))



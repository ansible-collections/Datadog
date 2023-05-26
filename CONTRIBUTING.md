# Contributing

The code is licensed under the Apache License 2.0 (see LICENSE for details).

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-Datadog.datadog-660198.svg)](https://galaxy.ansible.com/Datadog/datadog/)

First of all, thanks for contributing!

This document provides some basic guidelines for contributing to this repository. To propose improvements, feel free to submit a PR.

## Submitting issues

* If you think you've found an issue, search the issue list to see if there's an existing issue.
* Then, if you find nothing, open a Github issue.

## Pull Requests

All changes concerning the `datadog.dd.agent` role must be directed to the [ansible-datadog](https://github.com/DataDog/ansible-datadog) repository. If your change concern the collection in itself we're more than happy to review your contribution in this repository !

In order to ease/speed up our review, here are some items you can check/improve when submitting your PR:

  * Have a proper commit history (we advise you to rebase if needed).
  * Write tests for the code you wrote.
  * Preferably, make sure that all unit tests pass locally and some relevant kitchen tests.
  * Summarize your PR with an explanatory title and a message describing your changes, cross-referencing any related bugs/PRs.
  * Open your PR against the `master` branch.

### Keep it small, focused

Avoid changing too many things at once. For instance if you're fixing a recipe and at the same time adding some code refactor, it makes reviewing harder and the _time-to-release_ longer.

### Commit messages

Please don't be this person: `git commit -m "Fixed stuff"`. Take a moment to write meaningful commit messages.

The commit message should describe the reason for the change and give extra details that will allow someone later on to understand in 5 seconds the thing you've been working on for a day.

If your commit is only shipping documentation changes or example files, and is a complete no-op for the test suite, add **[skip ci]** in the commit message body to skip the build and give that slot to someone else who does need it.

### Squash your commits

Rebase your changes on `master` and squash your commits whenever possible. This keeps history cleaner and easier to revert things. It also makes developers happier!

## Development

To contribute, follow the contributing guidelines above.

### Manual testing

To test the roles provided by this project, you can follow the instructions in the manual tests [readme.md][tests].

## Author Information

brian@akins.org

dustinjamesbrown@gmail.com --Forked from brian@akins.org

Datadog <info@datadoghq.com> --Forked from dustinjamesbrown@gmail.com


[slack]: https://datadoghq.slack.com
[tests]: https://github.com/DataDog/ansible-datadog/blob/master/manual_tests/readme.md

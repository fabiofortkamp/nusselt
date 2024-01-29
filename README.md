# Nusselt

[![PyPI](https://img.shields.io/pypi/v/nusselt.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/nusselt.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/nusselt)][python version]
[![License](https://img.shields.io/pypi/l/nusselt)][license]

[![Read the documentation at https://nusselt.readthedocs.io/](https://img.shields.io/readthedocs/nusselt/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/fabiofortkamp/nusselt/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/fabiofortkamp/nusselt/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/nusselt/
[status]: https://pypi.org/project/nusselt/
[python version]: https://pypi.org/project/nusselt
[read the docs]: https://nusselt.readthedocs.io/
[tests]: https://github.com/fabiofortkamp/nusselt/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/fabiofortkamp/nusselt
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Development Guide

### First time setup

1. Install the multiple Python versions for testing with [asdf](https://asdf-vm.com):

```shell
asdf install python 3.8.18 3.9.18 3.10.13 3.11.7 3.12.1
```

2. Install [pipx](https://pipx.pypa.io/stable/) with [Homebrew](https://brew.sh):

```shell
brew install pipx
pipx ensurepath
```

3. Install required tools with:

```shell
pipx install poetry nox
pipx inject nox nox-poetry
```

4. Clone this repository and run `poetry install` inside it.

### Development Workflow

## User Installation

You can install _Nusselt_ via [pip] from [PyPI]:

```console
$ pip install nusselt
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Nusselt_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/fabiofortkamp/nusselt/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/fabiofortkamp/nusselt/blob/main/LICENSE
[contributor guide]: https://github.com/fabiofortkamp/nusselt/blob/main/CONTRIBUTING.md
[command-line reference]: https://nusselt.readthedocs.io/en/latest/usage.html

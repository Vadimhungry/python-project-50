# Difference Calculator

This is command line application. 
It can compare two files and show the difference between them.

## How to install

1. `git clone https://github.com/Vadimhungry/python-project-50.git`
2. `python3 -m pip install --user dist/*.whl`

## Usage
`gendiff [-h] [-f FORMAT] first_file second_file`

Compares two configuration files and shows a difference.

### positional arguments:
* `first_file`
* `second_file`

### optional arguments:
* -h, --help            show help message and exit
* -f FORMAT, --format FORMAT
                        set format of output
### formats available:
* stylish - default formatter
* plain - text style formatter
* json - output in form of json file

### examples of usage:

Step 5 (package work example):
[![asciicast](https://asciinema.org/a/GrhAwBvAWScgYvCo0RBLABRyO.svg)](https://asciinema.org/a/GrhAwBvAWScgYvCo0RBLABRyO)

Step 6(stylish formatter by default, work with nested json and yml):
[![asciicast](https://asciinema.org/a/KXYpsPd80csiSdfjgiYOwEK9A.svg)](https://asciinema.org/a/KXYpsPd80csiSdfjgiYOwEK9A)

Step 7(plain formatter):
[![asciicast](https://asciinema.org/a/gwhxHUoyG02dYSP5Z1HBd33qn.svg)](https://asciinema.org/a/gwhxHUoyG02dYSP5Z1HBd33qn)

Step 8(json formatter):
[![asciicast](https://asciinema.org/a/BlhenPcGWUXFDtxJUguM55aAL.svg)](https://asciinema.org/a/BlhenPcGWUXFDtxJUguM55aAL)

### Hexlet tests and linter status:
[![hexlet-check](https://github.com/Vadimhungry/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Vadimhungry/python-project-50/actions/workflows/hexlet-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/55e816a0053e58471fd9/maintainability)](https://codeclimate.com/github/Vadimhungry/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/55e816a0053e58471fd9/test_coverage)](https://codeclimate.com/github/Vadimhungry/python-project-50/test_coverage)

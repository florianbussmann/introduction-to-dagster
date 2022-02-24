# Introduction to Dagster

[![pytest](https://github.com/florianbussmann/introduction-to-dagster/actions/workflows/pytest.yml/badge.svg)](https://github.com/florianbussmann/introduction-to-dagster/actions/workflows/pytest.yml)

This repository contains some experiments with [Dagster](https://www.dagster.io/) based on their [tutorial](https://docs.dagster.io/tutorial).


## Setup environment
You can set up your development environment with:

```sh
source prepare-env.sh
```

## Hello, dagster
```sh
dagster job execute -f hello_world.py
dagit -f hello_world.py
```

## Running tests
During development, you might like to run tests.

```sh
python3 -m pytest
```
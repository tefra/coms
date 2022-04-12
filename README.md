# Numan Communications


# Clone Repo

```console
$ git clone git@github.com:BeaNuman/numan-coms.git
$ cd numan-coms
```

# Local Installation

This step requires to setup a virtual environment manually, I recommend [pyenv](https://github.com/pyenv/pyenv-installer)

```console
$ pyenv install 3.10-dev
$ pyenv virtualenv 3.10-dev numan-comns
$ pyenv activate numan-coms
$ pip install poetry
$ poetry install
```

## Hint

if you have a pyenv plugin hooked in your terminal, you can auto-activate the env each time you
enter the directory

```console
$ pyenv local numan-coms
```

## Start the app

```console
$ make start
```

## Running tests

```console
$ pytest tests/
$ pytest --cov=coms tests/  # with coverage report
```

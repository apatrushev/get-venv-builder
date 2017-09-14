# What and why?
Python2 is still alive in the wild and needs to be bootstrapped time to time.
This bootstrapping procedures can be complex if you do not want (or can not)
pollute system wide python env. You need to create virtual environment, but
venv package became part of stdlib only since Python 3.3.

This package helps to create bootstrap scripts. Also you can create your
own scripts which will do some additional actions after creating virtual
environment.

You can find examples of such custom additional actions in
the [examples directory](examples).

Target bootstrap script will create clean virtual environment in `venv` subfolder
of current directory on run.

## Prepare
### Build
```shell
pip wheel --no-deps -w . .
```

### Install
From PyPI:
```
[COMING SOON] pip install get-venv-builder
```
... to clean separate venv (dogfooding):
```shell
curl -L https://raw.githubusercontent.com/apatrushev/get-venv-builder/master/bootstrap.py | python
```

## Use
### Create bootstrap script
Just execute console script:
```shell
gvb
```
... or package as module:
```shell
python -m get_venv_builder
```
Default name for result script is `get-venv.py`.

### CLI docs
```shell
# gvb --help
Usage: gvb [OPTIONS]

Options:
  --output TEXT         Output filename.
  --post-code FILENAME  Path to post create code.
  --help                Show this message and exit.
```

### Custom post-actions
Create your action as python script and provide it to bootstrap creator:
```python
import subprocess
VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
subprocess.check_call([VENV_PYTHON,] + '-m pip install lektor'.split())
```
... and build your custom bootstrap script:
```shell
gvb --post-code your-script.py
```

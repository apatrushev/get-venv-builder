# What and why?
Python2 is still alive in the wild and needs to be bootstrapped time to time.
This bootstrapping procedures can be complex if you do not want (or can not)
pollute system wide python env. You need to create virtual environment, but
venv package is part of stdlib only since Python 3.3.

This package creates such bootstrapping scripts. You can create your own scripts
which will do some additional actions after creating virtual environment.

You can find examples of such custom additional actions in
the [examples directory](examples).

## Build
```shell
pip wheel --no-deps -w . .
```

## Install
One of the following:
```shell
pip install .
pip install -e .
[COMING SOON] pip install get-venv-builder
[COMING SOON] curl -L [some-fixme-url] | python
```

## Use
### Create bootstrapping script
Just execute package as module:
```shell
python -m get-venv-builder
```
... or console script:
```shell
gvb
```
Default name for result script is ```get-venv.py```.

### CLI docs
```shell
# gvb --help
Usage: gvb [OPTIONS]

Options:
  --output TEXT         output filename
  --post-code FILENAME  path to post create code
  --help                Show this message and exit.
```

### Custom post-actions
Just create your action as python script and provide it to bootstrap creator:
```python
import os
VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
os.system('{0} -m pip install lektor'.format(VENV_PYTHON))
```
... and build your custom bootstrap script:
```shell
gvb --post-code your-script.py
```

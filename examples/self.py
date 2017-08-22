import os
VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
URL = 'git+https://github.com/apatrushev/get-venv-builder'
os.system('{0} -m pip install {1}'.format(VENV_PYTHON, URL))

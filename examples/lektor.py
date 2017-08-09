import os
VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
os.system('{0} -m pip install lektor'.format(VENV_PYTHON))

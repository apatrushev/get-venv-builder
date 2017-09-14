import subprocess
VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
subprocess.check_call([VENV_PYTHON,] + '-m pip install lektor'.split())

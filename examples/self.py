import subprocess
VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
URL = 'git+https://github.com/apatrushev/get-venv-builder'
subprocess.check_call([VENV_PYTHON,] + '-m pip install'.split() + [URL,])

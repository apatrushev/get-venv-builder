import contextlib
import os
import sys

VENV_PYTHON = globals().get('VENV_PYTHON', 'python')

@contextlib.contextmanager  # noqa
def chdir(target):
    last = os.getcwd()
    os.chdir(target)
    yield
    os.chdir(last)

if sys.platform == 'darwin':  # noqa
    vbox_path = '/Applications/VirtualBox.app/Contents/MacOS'  # noqa
    os.environ['VBOX_INSTALL_PATH'] = vbox_path
    sdk_install = 'installer'
elif sys.platform == 'win32':
    vbox_path = os.environ['VBOX_MSI_INSTALL_PATH']
    sdk_install = 'install'
with chdir(os.path.join(vbox_path, 'sdk', sdk_install)):
    cmd = '{0} vboxapisetup.py build --build-base . --build-lib . install'
    os.system(cmd.format(VENV_PYTHON))
if sys.platform == 'win32':
    cmd = '{0} -m pip install pypiwin32'
    os.system(cmd.format(VENV_PYTHON))

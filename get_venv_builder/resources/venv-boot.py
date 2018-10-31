from __future__ import print_function
from contextlib import closing, contextmanager
import glob
import os
import re
import sys
import tarfile
import tempfile
import shutil
import ssl
import subprocess
try:
    from urllib2 import urlopen
    from StringIO import StringIO
except ImportError:
    from urllib.request import urlopen
    from io import BytesIO as StringIO

PYPI_VENV_PAGE = 'https://pypi.org/project/virtualenv/'
INITIAL_ENV = 'py-env0'


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


@contextmanager
def removable_tempdir():
    target = tempfile.mkdtemp()
    yield target
    shutil.rmtree(target)


# sanity check
if os.path.exists(INITIAL_ENV) or ():
    raise RuntimeError('env directory already exists')
elif len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    raise RuntimeError('second stage env directory already exists')

# fetch venv url
with closing(urlopen(PYPI_VENV_PAGE, context=ctx)) as resp:
    if resp.getcode() != 200:
        raise RuntimeError('Wrong response receive from PyPI')
    dist_url = None
    for line in resp:
        m = re.match(b'.*<a href=".*(https.*virtualenv.*tar.gz)">.*', line)
        if m is not None:
            dist_url = m.groups()[0]
if dist_url is None:
    raise RuntimeError('virtualenv dist not found')


# Fetch virtualenv from PyPI
with closing(urlopen(dist_url.decode(), context=ctx)) as resp:
    if resp.getcode() != 200:
        raise RuntimeError('Wrong response receive from PyPI')
    data = resp.read()


# Untar
data = StringIO(data)
with removable_tempdir() as temp_dir:
    with closing(tarfile.open(fileobj=data)) as data:
        data.extractall(temp_dir)

    venv_py = glob.glob(os.path.join(
        temp_dir,
        '*',
        'virtualenv.py'
    ))
    if not venv_py:
        venv_py = glob.glob(os.path.join(
            temp_dir,
            '*',
            '*',
            'virtualenv.py'
        ))
    venv_py = venv_py[0]

    # Create the initial env
    subprocess.check_call((sys.executable, venv_py, INITIAL_ENV))

# Second stage
if len(sys.argv) > 1:
    bin_folder = 'bin' if sys.platform != 'win32' else 'Scripts'
    venv_python = os.path.join(INITIAL_ENV, bin_folder, 'python')
    subprocess.check_call([venv_python,] + '-m pip install virtualenv'.split())
    subprocess.check_call([venv_python,] + '-m virtualenv'.split() + [sys.argv[1],])
    shutil.rmtree(INITIAL_ENV)

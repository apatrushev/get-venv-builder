from __future__ import print_function
from contextlib import closing, contextmanager
import os
import re
import sys
import tarfile
import tempfile
import shutil
import ssl
try:
    from urllib2 import urlopen
    from StringIO import StringIO
except ImportError:
    from urllib.request import urlopen
    from io import BytesIO as StringIO

PYPI_VENV_PAGE = 'https://pypi.python.org/pypi/virtualenv'
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
        m = re.match(b'.*(https.*virtualenv.*tar.gz).*md5.*', line)
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
    venv_py = os.path.join(
        temp_dir,
        os.listdir(temp_dir)[0],
        'virtualenv.py'
    )

    # Create the initial env
    os.system('{0} {1} {2}'.format(sys.executable, venv_py, INITIAL_ENV))

# Second stage
if len(sys.argv) > 1:
    bin_folder = 'bin' if sys.platform != 'win32' else 'Scripts'
    venv_python = os.path.join(INITIAL_ENV, bin_folder, 'python')
    os.system('{0} -m pip install virtualenv'.format(venv_python))
    os.system('{0} -m virtualenv {1}'.format(venv_python, sys.argv[1]))
    shutil.rmtree(INITIAL_ENV)

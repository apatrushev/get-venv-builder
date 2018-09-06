"""ATTENTION!!!
This is autogenerated file. Please change it
only in case if you know what you are doing
cmd: gvb --post-code examples/self.py --output bootstrap.py
"""
import base64
import contextlib
import logging
import os
import shutil
import sys
import tempfile
import zlib
import subprocess


VENV_FOLDER = 'venv'
VENV_PYTHON = os.path.join(
    os.path.abspath(VENV_FOLDER),
    'Scripts' if sys.platform == 'win32' else 'bin',
    'python'
)
VENV_BOOT_DATA = """eNrFVUuP2zYQvutXsMlBkutwN9tbUAdNA6cwUDhGNg8Ui4VASyOLG4lkyZFj
5dd3SFmPbJ0WPdUXczjDmW++eai0umFZVrbYWsgyJhujLTJjpUK6VTlKraLSW+VaIZywlvvBKq+1k+qw
HFSNUOIANjqrtRtOFoaT68ZLFLaU9ahBaMxcdlWLsh4lNx3bvbE6B+citN2LiNEvAGxtTeBuBnQkagNq
0t8iZXXYvB0MBjmCUw4G2SZcr63V9m9euYU/W3D4XedSD6pfOwRHUYSbIkS7P3ab7ON6+zHbvfptzVYs
rhCNe3F1ZTojubaHK0rqAXK8OkqLrahBHa/iaLPdvN+8+j2jl/6R6Z7R/XUcRVGOJ7ohXnhuQSBkBZSi
rTE7FyNJvQnPK8g/Z5V2qEQD9OKNqB0E1RGsLLus0QWcPb1ev3ufbd9u1+T/l0dFJfdUx0Yfxb6GzFer
kDZJe6aolgdA8jJUkTefC38mFF7fSaiLs1W46KvLbYMWIOkVKUV9ypxQEjsWcEeypC7iRmDF4SQdumRG
SMq0ZQMCK6QD9q5VKBsINUxioooRSCJV246JmngqOtY7itMIanJPPCfUlJwQHFP2kj1nQhWPgw4Gd8/v
/yGcA6KsYA6JL/YvsSnREjCv2NEbUjdFXyRWw0Ql5/ZKvm2bcdBWVL409R1mwZkekSyDwInInCqapOyH
Fbu5vu6138P8yWp1CA+1IiXhBXmEvqV33W4T9/UrCHZGoKjCW62gb3tiv5YKmFQzGP7XkJmlFhCUYLKP
+eJnwSoL5eoJXySh7/li6nK+oPLzw9f0yUu+iJfBZzr6orRouBxTGkPoKcojXA0/WN0al6R31/e+cUYd
vZ5eXiJhwhIehVilblUR9y35pq/UZDXSc7lqQ2ReQF+K/7FwAkWoBgXwLZj0GX1QxHl0Vg5bKvFy2qd0
YdI9ai9kJPXYvkn+vM55YMCf9P5hFTyGl/40ZeQlGi60IkdR18ngtwftZyIzHUEb5vBBS5WMrwfr5XhD
djWR7nGOrqgNJoNZjbnp4nBPVPi/p+x1WKAMK9/LEqWo/fj2e2r82Jw3ae7hhoUAJ8hb9BwtB8RLNl9P
YcpvZ0shurRvelL2UmWlrguwfs2TFPu+8IamFkij1viuiL9I9dNNzIBWOItvcysNbZM5Z1hp9Zi3Gabl
LNDSf068/blVLqd6N3O8vGc/svhZw4w0xJTzpZuNRcydqSV9eP6zvws+SHM3W7vL+/TCd2PO9l/7H+aB
"""


@contextlib.contextmanager
def removable_tempdir():
    target = tempfile.mkdtemp()
    yield target
    shutil.rmtree(target)


def main(executable, *args):
    if os.path.exists(VENV_FOLDER) and '--renew' in args:
        shutil.rmtree(VENV_FOLDER)

    if not os.path.exists(VENV_FOLDER):
        with removable_tempdir() as temp_dir:
            venv_boot_filename = os.path.join(temp_dir, 'venv-boot.py')
            data = base64.b64decode(VENV_BOOT_DATA)
            data = zlib.decompress(data)
            with open(venv_boot_filename, 'wb') as venv_boot_file:
                venv_boot_file.write(data)

            subprocess.check_call((
                sys.executable,
                venv_boot_filename,
                VENV_FOLDER
            ))

        try:
            post_create()
        except:
            logging.exception('post create code failed')
            shutil.rmtree(VENV_FOLDER, ignore_errors=True)


def post_create():
    import subprocess
    VENV_PYTHON = globals().get('VENV_PYTHON', 'python')
    URL = 'git+https://github.com/apatrushev/get-venv-builder'
    subprocess.check_call([VENV_PYTHON,] + '-m pip install'.split() + [URL,])
    pass


if __name__ == '__main__':
    main(*sys.argv)

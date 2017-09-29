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
VENV_BOOT_DATA = ''


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
    # POST_CREATE_CODE
    pass


if __name__ == '__main__':
    main(*sys.argv)

"""ATTENTION!!!
This is autogenerated file. Please change it
only in case if you know what you are doing
cmd: gvb --output clean.py
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


VENV_FOLDER = os.environ.get('VENV_FOLDER', 'venv')
VENV_PYTHON = os.path.join(
    os.path.abspath(VENV_FOLDER),
    'Scripts' if sys.platform == 'win32' else 'bin',
    'python'
)
VENV_BOOT_DATA = """eNrFVUuP2zYQvutXsMlBkuvQm+0tqIOmgVMYKBwjmweKxUKgpZHNDUWqJOVY
+fUdUqKk3Sh9nKqDwOEMZ775ZjgstapIlpWNbTRkGeFVrbQltebS4q7MLVcyKp1VrqSFixX8EKxyoQyX
x2VQVUyyI+ioVx+FOoS1MmGlIaxMO2xapksuBo2Fqp7K5tRYLgbJjMvmUGuVgzGR1e2LiODnwTZaINDr
gBRFVYMc9TcWMzxu3waDIEdwyaG2ZOu3N1or/Y1XquHPBoz9rnOugurX1oLBKMyMEaL9H/tt9nGz+5jt
X/22IWsSn6ytzYvVqm5rTpU+rjCpe8jt6sy1bZgAeV7F0Xa3fb999XuGJ92hun2G+1dxFEW5veAO8kJz
DcxCVkDJGmGzvjBJ6kxofoL8c3ZSxkpWAZ54w4QBrzqD5mWbVaqA3tPrzbv32e7tboP+f3lUYHSPdazU
mR0EZK5aBddJ2jGFtTyCRS+hirT6XLg1onD6loMoeiu/0VWX6spqgKRTpBj1KTFMctsSjzviJXYRrZk9
UbhwY00yISQlSpOAQDNugLxrpOUV+BomMVJFECSSqnRLmECeipZ0juI0AoHukecEm5IignNKXpLnhMni
cdBgcPv87m/CGUDKCmIs8kX+ITYmWoLNT+TsDLGboi/cnsLtSvr2Sh62zXDp1li+NHUdpsHUHSJeeoEi
kTlWNEnJD2tyfXXVab+H+ZNW8ugPKolKxAv8DF1L79v9Nu7qVyDsDEFhhXdKQtf2yL7gEgiXExjuq9BM
YwswTDA5xHTxMyMnDeX6CV0kvu/pYuxyusDy0+PX9MlLuoiX3mc6+MK08HIZIpX1occoj3BV9KhVU5sk
vb26c40z6PD0eHKOhBGLP+RjlaqRRdy15JuuUqPVQM981UJkWkBXiv+xcMwyXw0M4Fow6TL6IJHzqFeG
KZU4Oe1SmrnpDrUTMpQ6bA+S78c59Qy4lTrcr71Hf9KtxoychJfLapZbJkQS/CI6p3aXIqtbxObeE+p+
SbiS94rLZHAUDi6HnRh7aBQmbVa3sd9P00C7q3MfaoT272PPx/8Gw/zGDLAJuBFEv3I97TVPyWs/7ok9
uZvHLWfCDZtuqg5PYz/3c0euH19wgbyxrqLL4HNJpsPUz6SbyQiL5qZjx9OBy6xUogDtHiWUYkenM6wF
szgYKtfD8Rcuf7qOCeCDQ+KbXPMaZ980P3tSEj08oHeCaTkJtHSPn7PvG3s+1duJ4+Ud+ZHEzypS8xqZ
Mq7RJpc4pqYWHJ/J/+xvxgdqbiePxPIunXnlpmz/Ba0wE8I=
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
    # POST_CREATE_CODE
    pass


if __name__ == '__main__':
    main(*sys.argv)
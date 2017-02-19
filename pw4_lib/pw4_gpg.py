import getpass
import os
import sys

import gnupg

from pw4_lib import platformSystem
from pw4_lib.fakes import FakeGpg


class GpgProvider:
    def __init__(self):
        self.pwName = sys.argv[1]
        self.thePass = getpass.getpass(prompt="\033[3;32mDecryption Passphrase: \033[0m")

        self.home_dir = os.path.join(
            os.environ.get("HOME"),
            ".gnupg"
        )
        self.passwords_file = os.path.join(
            self.home_dir,
            'pw4.ini.gpg'
        )

        if platformSystem == 'Linux':
            self.gpg = gnupg.GPG(
                gnupghome=self.home_dir
            )
        elif platformSystem == 'Darwin':
            self.gpg = gnupg.GPG(
                gnupghome=self.home_dir,
                gpgbinary="/usr/local/Cellar/gnupg2/2.0.30_3/bin/gpg"
            )
        else:
            self.gpg = FakeGpg()

        with open(self.passwords_file, 'rb') as f:
            status = self.gpg.decrypt_file(
                f,
                passphrase=self.thePass
            )

        if status.ok:
            self.plaintext = str(status)
        else:
            raise Exception("no str")

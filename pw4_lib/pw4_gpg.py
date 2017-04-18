import StringIO
import getpass
import sys

import gnupg
import os

from pw4_lib import platformSystem
from pw4_lib.fakes import FakeGpg


class GpgProvider:
    @property
    def pw_prompt(self):
        return "\033[3;32mDecryption Passphrase: \033[0m"

    @property
    def the_gpg(self):
        if platformSystem == 'Linux':
            return gnupg.GPG(
                gnupghome=self.home_dir,
                verbose=self.verbose
            )
        elif platformSystem == 'Darwin':
            return gnupg.GPG(
                gnupghome=self.home_dir,
                gpgbinary="/usr/local/bin/gpg",
                verbose=self.verbose
            )
        else:
            return FakeGpg()

    def __init__(self, options):
        self.verbose = options.verbose
        self.pwName = sys.argv[1]
        self.thePass = getpass.getpass(prompt=self.pw_prompt)

        self.home_dir = os.path.join(
            os.environ.get("HOME"),
            ".gnupg"
        )
        self.passwords_file = os.path.join(
            self.home_dir,
            'pw4.ini.gpg'
        )

        with open(self.passwords_file, 'rb') as f:
            status = self.the_gpg.decrypt_file(
                f,
                passphrase=self.thePass
            )

        if status.ok:
            self.plaintext = str(status)
        else:
            raise Exception("no str")

    def show_possible_recipients(self):
        the_public_uids = (key['uids'][0] for key in
                           self.the_gpg.list_keys(True))
        the_private_uids = (key['uids'][0] for key in
                            self.the_gpg.list_keys(False))

        for each_key in the_public_uids:
            if each_key in the_private_uids:
                print each_key

    def save_and_encrypt(self, the_config):
        print "AVAILABLE ENCRYPTION KEYS:"
        self.show_possible_recipients()
        the_recipients = raw_input('Enter recipient(s): ')
        output = StringIO.StringIO()
        the_config.write(output)
        the_crypted_thing = self.the_gpg.encrypt(
            output.getvalue(),
            recipients=the_recipients.split(',')
        )
        output.close()

        with open(self.passwords_file, 'w') as f:
            f.write(the_crypted_thing.data)
            f.close()

        new_all_keys = ' '.join(the_config.sections())
        all_file_name = os.path.join(
            os.environ.get('HOME'),
            '.gnupg',
            'pw4-all.txt'
        )

        with open(all_file_name, 'w') as all_sections_file:
            all_sections_file.write(new_all_keys)
            all_sections_file.close()

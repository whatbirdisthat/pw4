import os
import platform
import gnupg

platformSystem = platform.system()
if platformSystem not in ("Linux", "Darwin"):
    raise Exception("WINDOWS IS NOT SUPPORTED :(")

def ProvideGPG():
    home_dir = os.environ.get("HOME") + "/.gnupg"
    if platformSystem == 'Linux':
        gpg = gnupg.GPG(
            gnupghome=home_dir
        )
    elif platformSystem == 'Darwin':
        gpg = gnupg.GPG(
            gnupghome=home_dir,
            gpgbinary="/usr/local/Cellar/gnupg2/2.0.30_3/bin/gpg"
        )
    else:
        gpg = fakeGpg()

    return gpg


def print_usage():
    print """
pw4 - a mimetic password retrieval and management system
actually it's a tiny little script that does actually
very little.

usage: pw4 <account>

pw4 supports tab completion.

"""


class fakeGpg:
    def GPG(self, **kwargs):
        pass

    def decrypt_file(self, the_file):
        pass

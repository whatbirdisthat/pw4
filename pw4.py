#!/usr/bin/env python

import ConfigParser
import StringIO
import getpass
import os
import sys

import gnupg
import pyperclip

if __name__ == '__main__':

    pwName = sys.argv[1]
    thePass = getpass.getpass()
    home_dir = os.environ.get("HOME") + "/.gnupg"

    gpg = gnupg.GPG(
        gnupghome=home_dir,
        gpgbinary="/usr/local/Cellar/gnupg2/2.0.30_3/bin/gpg"
    )

    with open(os.environ.get('HOME') + '/secure/pw.ini.gpg', 'rb') as f:
        status = gpg.decrypt_file(
            f,
            passphrase=thePass
        )

    plaintext = ''
    if status.ok:
        plaintext = str(status)
    else:
        print "no str"
        exit(1)

    buf = StringIO.StringIO(plaintext)
    config = ConfigParser.ConfigParser()
    config.readfp(buf)

    if not config.has_section(pwName) or pwName == 'all':
        print ' '.join(config.sections())
        exit(0)

    if config.has_option(pwName, 'Account'):
        theAc = config.get(pwName, 'Account')
        print "Account: {}".format(theAc)

    if config.has_option(pwName, 'Username'):
        theUn = config.get(pwName, 'Username')
        print "Username: {0}".format(theUn)

    if config.has_option(pwName, 'Password'):
        thePW = config.get(pwName, 'Password')
        pyperclip.copy(thePW)
    else:
        print "No password found: nothing put on the clipboard"

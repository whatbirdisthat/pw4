#!/usr/bin/env python

import ConfigParser
import StringIO
import getpass
import os
import sys

import pyperclip

from pw4_lib import ProvideGPG, print_usage

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print_usage()
        exit(1)

    pwName = sys.argv[1]
    thePass = getpass.getpass()

    gpg = ProvideGPG()

    with open(os.environ.get('HOME') + '/secure/pw4.ini.gpg', 'rb') as f:
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

    config = ConfigParser.ConfigParser()
    buf = StringIO.StringIO(plaintext)
    config.readfp(buf)
    # When Python 3 is like actually a thing:
    # config.read_string(plaintext)

    if not config.has_section(pwName) or pwName == 'all':
        print ' '.join(config.sections())
        exit(0)

    for x, y in config.items('pwName'):
        if not x == 'Password':
            print '{}: {}'.format(x, y)

    if config.has_option(pwName, 'Password'):
        thePW = config.get(pwName, 'Password')
        pyperclip.copy(thePW)
    else:
        print "No password found: nothing put on the clipboard"

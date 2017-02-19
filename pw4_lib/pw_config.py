import ConfigParser
import StringIO

import pyperclip

from pw4_lib import print_usage


class ConfigProvider:
    def __init__(self, plaintext):
        self.config = ConfigParser.ConfigParser()
        # When Python 3 is like actually a thing:
        # config.read_string(plaintext)
        buf = StringIO.StringIO(plaintext)
        self.config.readfp(buf)

    def print_all_sections(self):
        print ' '.join(self.config.sections())

    def print_section(self, pw_name):
        if not self.config.has_section(pw_name):
            print_usage()
            exit(1)

        for x, y in self.config.items(pw_name):
            if x not in ('Password', 'password'):
                print '{}: {}'.format(x, y)

        if self.config.has_option(pw_name, 'Password'):
            the_pw = self.config.get(pw_name, 'Password')
            pyperclip.copy(the_pw)
        else:
            print "No password found: nothing put on the clipboard"

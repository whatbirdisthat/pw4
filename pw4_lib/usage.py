from pw4_lib.pw4_options import OptionsProvider


def print_usage():
    print """
pw4 - a mimetic password retrieval and management system
actually it's a tiny little script that does actually
very little.

pw4 supports tab completion.
"""
    OptionsProvider().parser.print_help()

    print """
Examples:
    pw4 NASA                    print the account details for NASA and put the password on the clipboard
    pw4 NA<TAB>                 initiate autocomplete
    pw4 --all                   print all the account names
    pw4 --all > names.txt       print all the account names to a file, such as the file that is read by
                                the pw4 bash completion script


Copyright 2016 What Bird Is That?
Written by whatbirdisthat.github.io

This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

"""


def print_version():
    print """
pw4 1.0
"""

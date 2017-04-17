from optparse import OptionParser


class OptionsProvider:
    def __init__(self):
        self.parser = OptionParser(add_help_option=False)
        self.parser.add_option(
            '-a', '--all',
            action='store_true', default=False,
            help="Print All Password Groups to stdout"
        )
        self.parser.add_option(
            '-n', '--new',
            action='store_true', default=False,
            help="Add a new pw group"
        )
        self.parser.add_option(
            '-h', '--help',
            action='store_true', default=False,
            help="Print help text and exit"
        )
        self.parser.add_option(
            '-v', '--version',
            action='store_true', default=False,
            help="Print version and exit"
        )
        self.parser.add_option(
            '-b', '--verbose',
            action='store_true', default=False,
            help="Show verbose logging information"
        )
        (self.options, self.args) = self.parser.parse_args()

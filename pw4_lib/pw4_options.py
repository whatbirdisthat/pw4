from optparse import OptionParser


class OptionsProvider:
    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option(
            '-a', '--all',
            action='store_true', default=False,
            help="Print All Password Groups to stdout"
        )
        self.parser.add_option(
            '-v', '--version',
            action='store_true', default=False,
            help="Print version and exit"
        )
        (self.options, self.args) = self.parser.parse_args()
from pw4_lib.pw4_options import OptionsProvider


def print_usage():
    print """
pw4 - a mimetic password retrieval and management system
actually it's a tiny little script that does actually
very little.

pw4 supports tab completion.
"""
    provider = OptionsProvider()
    provider.parser.print_help()

    print """
"""
#!/usr/bin/env python

from pw4_lib.pw4_gpg import GpgProvider
from pw4_lib.pw4_options import OptionsProvider
from pw4_lib.pw_config import ConfigProvider

if __name__ == '__main__':
    options = OptionsProvider().options
    gpg_provider = GpgProvider()
    config_provider = ConfigProvider(gpg_provider.plaintext)
    if options.all:
        config_provider.print_all_sections()
    else:
        config_provider.print_section(gpg_provider.pwName)

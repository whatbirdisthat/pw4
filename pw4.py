#!/usr/bin/env python

from pw4_lib.pw4_gpg import GpgProvider
from pw4_lib.pw4_options import OptionsProvider
from pw4_lib.pw_config import ConfigProvider
from pw4_lib.usage import print_version, print_usage

if __name__ == '__main__':
    options = OptionsProvider().options
    if options.version:
        print_version()
        exit(0)
    if options.help:
        print_usage()
        exit(0)

    gpg_provider = GpgProvider(options)
    config_provider = ConfigProvider(gpg_provider.plaintext)

    if options.all:
        config_provider.print_all_sections()
    elif options.new:
        section_name = config_provider.add_section()
        gpg_provider.save_and_encrypt(config_provider.config)
        config_provider.print_section(section_name)
    else:
        config_provider.print_section(gpg_provider.pwName)

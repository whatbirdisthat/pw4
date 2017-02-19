
import sys
import platform
from pw4_lib.usage import print_usage

platformSystem = platform.system()
if platformSystem not in ("Linux", "Darwin"):
    raise Exception("WINDOWS IS NOT SUPPORTED :(")

if len(sys.argv) < 2:
    print_usage()
    exit(1)


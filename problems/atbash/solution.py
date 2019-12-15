#!/usr/bin/env python3

import sys

z = ord('z')
a = ord('a')
for c in sys.argv[1]:
    print('\n' if c == '\n' else chr(z - (ord(c) - a)), end="")

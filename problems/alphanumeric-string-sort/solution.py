#!/usr/bin/env python3

import sys

print(''.join(sorted(sys.argv[1], key="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0246813579".index)))

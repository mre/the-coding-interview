#!/usr/bin/env python3
import sys

print(sum([(int((int(line) // 3)) - 2) for line in sys.argv[1].splitlines()]))

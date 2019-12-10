#!/usr/bin/env python3
import sys

fuel = 0
for line in sys.argv[1].splitlines():
    x = int(line)
    while x > 0:
        x = max(0, x // 3 - 2)
        fuel += x
print(fuel)

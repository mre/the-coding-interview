import sys
import math

"""
One could start with the total amount of paint available and reduce it by the amount which is needed to draw a circle with radius r until nothing is left.


Radius   Tint
-------------
1         (1^2)*pi
2         (2^2)*pi
...
n         (n^2)*pi


We start with a "white ring" with an area of (r^2)*pi.
The first ring has radius r+1 and area (r+1)^2*pi.
Therefore we need (r+1)^2 *pi - r^2*pi mililiters of tint to draw the ring (substract the inner white area).
=> tint = ((r+1)^2 - r^2)*pi = (r^2 + 2r + 2 - r^2)*pi = (2r+1)*pi for ring 1.

For ring two: tint = ((r+3)^2 - (r+2)^2)*pi = (r^2+6r+9 - r^2-4r-4)*pi = (2r+5)*pi

Radius of nth ring = r_n = r+2*(n-1)+1 = r+2n-1
For nth ring: tint = ((r+2n-1)^2-(r+2n-2)^2)*pi = (r^2+2rn-r+2rn+4n^2-2n-r-2n+1-r^2-2rn+2r-2rn-4n^2+4n+2r+4n-4)*pi
= (2r+4n-3)*pi


We need the sum of tint for all n rings, i.e.:
tint = tint_1 + tint_2 + ... + tint_n = (2r+1)*pi + (2r+5)*pi + ... + (2r+4n-3)*pi
= 2*r*pi*(1+5+...+4n-3)

tint = 2*r*pi*sum(4n-3 for n in rings)

avail_tint >= 2*r*pi*sum(4n-3 for n in rings)

<=> avail_tint/2rpi >= sum(4n-3 for n in rings)
"""

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      r, t = map(int, sys.stdin.readline().split())
      yield (case, r, t)

def solve(r, t):
  n = 1 # Current ring
  print "tint", t
  sum_tint = 0
  remaining = int(math.floor(t/math.pi))
  while True:
    sum_tint += 2*r+4*n-3
    if sum_tint > remaining:
      return n
    n += 1

def main():
  for case, r, t in get_data():
    print("Case #{}: {}".format(case, solve(r, t)))

if __name__ == "__main__":
  main()


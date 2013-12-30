import sys
from math import ceil, floor, sqrt

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      start, stop = [int(v) for v in sys.stdin.readline().strip().split()]
      yield (case, start, stop)

def fair(i):
  string = str(i)
  return string == string[::-1]

def check_range(start, stop):
  n = 0
  sstart = ceil(sqrt(start))
  sstop = ceil(sqrt(stop))+1
  for i in range(sstart, sstop):
    if fair(i) and fair(i**2):
      if i**2 <= stop:
        n += 1
  return n

def main():
  starts = []
  stops = []
  for case, start, stop in get_data():
    print("Case #{}: {}".format(case, check_range(start, stop)))

if __name__ == "__main__":
  main()

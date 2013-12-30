import sys

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      start, stop = [int(v) for v in sys.stdin.readline().strip().split()]
      yield (case, start, stop)

def fair(i):
  string = str(i)
  return string == string[::-1]

def check(i):
  return (i%2 != 0 and fair(i))

def check_range(start, stop):
  for i in range(start, stop):
    if i%9999999 == 0:
      print(i)
    """
    #if check(i):
    #  print(i)
    """

def main():
  starts = []
  stops = []
  for case, start, stop in get_data():
    starts.append(start)
    stops.append(stop)

  # Find the lowest start
  min_start = min(starts)
  # Find the highest stop
  max_stop = max(stops)

  #check_range(min_start, max_stop)
  check_range(0,10**100)

  """
    print "Case #" + repr(case) + ":", start, stop #solve(data)
    for line in data:
      print " ".join([str(i) for i in line])
    print
  """

if __name__ == "__main__":
  main()

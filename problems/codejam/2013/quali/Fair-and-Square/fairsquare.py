import sys

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      start, stop = [int(v) for v in sys.stdin.readline().strip().split()]
      yield (case, start, stop)

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

  print min_start, max_stop

  """
    print "Case #" + repr(case) + ":", start, stop #solve(data)
    for line in data:
      print " ".join([str(i) for i in line])
    print
  """

if __name__ == "__main__":
  main()

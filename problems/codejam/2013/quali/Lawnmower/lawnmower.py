import sys, time

def get_data():
    numcases = int(sys.stdin.readline())
    for case in range(1,numcases+1):
        N, M = [int(v) for v in sys.stdin.readline().strip().split()]
        data = []
        for line_number in range(N):
            line = sys.stdin.readline().strip().split()
            data.append([int(i) for i in line])
        yield (case, data)

def below_max_height(lawn, max_height = 100):
  for line in lawn:
    if any(field < 1 or field > max_height for field in line):
      return "NO"
  return "YES"

def solve(lawn):
  # Take highest setting as pattern
  heights = [sum(int(i) for i in line) for line in lawn]
  max_line = heights.index(max(heights))
  pattern = lawn[max_line]

  # Check all other lines against this pattern
  other_lines = lawn[:max_line] + lawn[max_line+1:]
  for line in other_lines:
    if line != pattern:
      setting = max(line)
      trimmed = [min(setting, p) for p in pattern]
      if line != trimmed:
        return "NO"
  return below_max_height(lawn)

def main():
    for case, data in get_data():
      print "Case #" + repr(case) + ":", solve(data)
      """
      for line in data:
        print " ".join([str(i) for i in line])
      print
      """

if __name__ == "__main__":
  main()

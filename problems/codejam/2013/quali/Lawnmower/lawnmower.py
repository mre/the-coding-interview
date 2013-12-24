import sys, time

def get_data():
    numcases = int(sys.stdin.readline())
    for case in range(1,numcases+1):
        N, M = [int(v) for v in sys.stdin.readline().strip().split()]
        data = []
        for line_number in range(N):
            line = sys.stdin.readline().strip().split()
            data.append(line)
        yield (case, data)


def border_topbottom_ok(lawn):
  top = lawn[0]
  bottom = lawn[-1]
  length = len(lawn[0])
  # Exclude edges
  for i in range(1,length-1):
    if top[i] != bottom[i]:
      return False
  return True

def border_leftright_ok(lawn):
  # Exclude edges
  sides = lawn[1:-1]
  for row in sides:
    if row[0] != row[-1]:
      return False
  return True

def edges_ok(lawn):
  maxh = len(lawn)-1
  maxw = len(lawn[0])-1
  if lawn[0][0] != lawn[maxh][0] and \
     lawn[0][0] != lawn[0][maxw]:
      return False
  if lawn[maxh][maxw] != lawn[maxh][0] and \
     lawn[maxh][maxw] != lawn[0][maxw]:
      return False
  return True

def border_ok(lawn):
  """ Opposite edges must have same height """
  return border_topbottom_ok(lawn) and \
         border_leftright_ok(lawn) and \
         edges_ok(lawn)

def inner_ok(lawn):
  # Crop border to get inner lawn
  print lawn
  for y in range(1,len(lawn)-1):
    for x in range(1,len(lawn[0])-1):
      if lawn[y][x] != lawn[y][x-1] and \
         lawn[y][x] != lawn[y-1][x]:
           return False
  return True

def below_max_height(lawn, max_height = 100):
  for line in lawn:
    if any(1 <= field <= max_height for field in line):
      return False
  return True

def solve(lawn):
  if border_ok(lawn) and inner_ok(lawn) and \
     below_max_height(lawn):
      return "YES"
  return "NO"

def main():
    for case, data in get_data():
      print "Case #" + repr(case) + ":", solve(data)
      for line in data:
        print "".join(line)
      print

if __name__ == "__main__":
  main()

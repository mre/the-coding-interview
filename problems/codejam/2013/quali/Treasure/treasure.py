import sys
from collections import defaultdict

class Chest(object):
    def __init__(self, id, content):
        self.id, self.content = id, content

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      num_keys, num_chests = map(int, sys.stdin.readline().split())
      keys = map(int, sys.stdin.readline().split())
      # Store chests in dictionary
      chests = defaultdict(list)
      for id in range(1,num_chests+1):
        chest_data = map(int, sys.stdin.readline().split())
        unlock_key, content = chest_data[0], chest_data[2:]
        chest = Chest(id, content)
        chests[unlock_key].append(chest)
      yield (case, keys, chests)

def main():
  for case, keys, chests in get_data():
    print "Case", case
    print keys
    for k,v in chests.items():
        print k, ": ", ",".join(str(chest.id) for chest in v)
    print
    #print("Case #{}: {}".format(case, solve(start, stop)))

if __name__ == "__main__":
  main()


"""
def solve():

closed_chests = []
keys = []




if closed_chests and not keys:
    # Game over
    return "IMPOSSIBLE"
"""

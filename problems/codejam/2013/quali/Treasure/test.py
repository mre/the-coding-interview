from collections import defaultdict
import copy

"""
def unlock(chests, key, index = -1):
  chest = None
  matching_chests = chests.get(key)
  if matching_chests:
    chest = matching_chests.pop(index)
  return chest


class Chest(object):
    def __init__(self, id, content):
        self.id, self.content = id, content

def count(d):
    print(",".join(str(c.id) for v in d.values() for c in v))
    return sum(len(v) for v in d.values())


c1 = Chest(1,[1,2])
c2 = Chest(2,[3,4])
c3 = Chest(3,[4,5])

chests = defaultdict(list)
chests[1].append(c1)
chests[2].append(c2)
chests[2].append(c3)

print count(chests)


# TODO: Test extend!


keyring = [1,2,3]
content = [4]
new_keyring = keyring + content


def best_path(paths):
  rank = sorted(paths)
  return rank[0]


paths = [[2,1,3],[1,2,3],[3,1,2]]
print best_path(paths)
"""

def delfrom(key, dataset, item):
  d2 = copy.deepcopy(dataset)
  d2[key].remove(item)
  print "delfrom", d2
  return d2


def gentest(keys, dataset):
  for key in keys:
    for i in dataset[key]:
      remaining = delfrom(key, dataset, i)
      yield (i,remaining)

dataset = {1: [5, 23],2: [4,11]}
for i,j in gentest([1, 2], dataset):
  print i,j

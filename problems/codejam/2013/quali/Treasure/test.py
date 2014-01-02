from collections import defaultdict


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
    """ Count number of values in dict """
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


paths = []
print best_path(paths)

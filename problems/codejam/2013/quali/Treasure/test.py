from collections import defaultdict


def unlock(chests, key, index = -1):
  chest = None
  matching_chests = chests.get(key)
  if matching_chests:
    chest = matching_chests.pop(index)
  return chest

chests = defaultdict(list)
chests[1] = [1,2,3,4]

for index in chests.get(1):
  chest = unlock(chests, 1)
  print chest
  print chests

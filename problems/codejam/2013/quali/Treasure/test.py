from collections import defaultdict


def unlock(chests, key, index = -1):
  chest = None
  matching_chests = chests.get(key)
  if matching_chests:
    chest = matching_chests.pop(index)
  return chest

locked_chests = defaultdict(list)

def count(locked_chests):
  return sum(len(v) for v in locked_chests.itervalues())

locked_chests[1] = [1,2,3,4]
locked_chests[2] = [1,2,3,4]
if count(locked_chests):
  print "Work to do"
else:
  print "Done"

"""
for index in chests.get(1):
  chest = unlock(chests, 1)
  print chest
  print chests
"""


keyring = [1,1,2,3,4]
for key in set(keyring):
  print key
print keyring

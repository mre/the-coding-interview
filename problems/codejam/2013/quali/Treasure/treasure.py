import sys
from collections import defaultdict

class Chest(object):
    def __init__(self, id, content):
        self.id, self.content = id, content

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      num_keys, num_chests = map(int, sys.stdin.readline().split())
      keyring = map(int, sys.stdin.readline().split())
      # Store chests in dictionary
      chests = defaultdict(list)
      for id in range(1,num_chests+1):
        chest_data = map(int, sys.stdin.readline().split())
        unlock_key, content = chest_data[0], chest_data[2:]
        chest = Chest(id, content)
        chests[unlock_key].append(chest)
      yield (case, keyring, chests)

def count(d):
    """ Count number of values in dict """
    return sum(len(v) for v in d.itervalues())

def unlock(chests, key, index = -1):
    """ Get chest with matching key type from all chests """
    chest = None
    matching_chests = chests.get(key)
    if matching_chests:
        chest = matching_chests.pop(index)
    return chest

def get_all_paths(keyring, locked_chests, path = []):
    # If empty keyring and locked chests
    if not keyring and count(locked_chests):
        return "IMPOSSIBLE"
    # Take next key type from keyring
    for key in set(keyring):
        for chest in locked_chests[key]:
            # Add chest to path
            path.append[chest]
            # Add containing keys to keyring
            keyring.append(chest.content)

    # Have all chests been unlocked?
    if not count(locked_chests):
        # Success!
        yield path
    else:
        yield from get_all_paths(keyring, locked_chests, path)

def best_path(paths):
    pass

def solve(keyring, locked_chests):
    paths = get_all_paths(keyring, locked_chests)
    return best_path(paths)

def main():
  for case, keys, locked_chests in get_data():
    print("Case #{}: {}".format(case, solve(keys, locked_chests)))

if __name__ == "__main__":
  main()

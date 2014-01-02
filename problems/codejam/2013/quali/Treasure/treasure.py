import sys
from collections import defaultdict

class Chest(object):
    def __init__(self, id, content):
        self.id, self.content = id, content

def get_data():
  numcases = int(sys.stdin.readline())
  for case in range(1,numcases+1):
      num_keys, num_chests = map(int, sys.stdin.readline().split())
      keyring = list(map(int, sys.stdin.readline().split()))
      # Store chests in dictionary
      chests = defaultdict(list)
      for id in range(1,num_chests+1):
        chest_data = list(map(int, sys.stdin.readline().split()))
        unlock_key, content = chest_data[0], chest_data[2:]
        chest = Chest(id, content)
        chests[unlock_key].append(chest)
      yield (case, keyring, chests)

def count(d):
    """ Count number of values in dict """
    return sum(len(v) for v in d.values())

def unlock(key, chest, chests):
    """ Remove chest with matching key type from all chests """
    new_chests = chests.copy()
    new_chests[key].remove(chest)
    return new_chests

def get_all_paths(keyring, locked_chests, path = []):
    # Have all chests been unlocked yet?
    if not count(locked_chests):
        yield path # We are done
    # No luck if empty keyring and locked chests
    if not keyring:
        return None
    # We're not done yet.
    # Take next key type from keyring.
    for key in set(keyring):
        for chest in locked_chests[key]:
            # Add chest to path
            new_path = path + [chest.id]
            # Add containing keys to keyring
            new_keyring = keyring + chest.content
            # "Unlock" chest i.e. remove chest from dict.
            remaining_chests = unlock(key, chest, locked_chests)
            yield from get_all_paths(new_keyring, remaining_chests, new_path)

def best_path(paths):
    if not paths:
        return "IMPOSSIBLE"
    rank = sorted(paths)
    return " ".join(str(chest) for chest in rank[0])

def solve(keyring, locked_chests):
    paths = [p for p in get_all_paths(keyring, locked_chests) if p]
    return best_path(paths)

def main():
  for case, keys, locked_chests in get_data():
    print("Case #{}: {}".format(case, solve(keys, locked_chests)))

if __name__ == "__main__":
  main()

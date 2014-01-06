import sys
from collections import defaultdict, Counter
import copy

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

def remove_chest(chests, id):
    for index, chest in enumerate(chests):
        if chest.id == id:
            del chests[index]
            return

def unlock(key, chest, chests):
    """ Remove chest with matching key type from all chests """
    new_chests = copy.deepcopy(chests)
    remove_chest(new_chests[key], chest.id)
    return new_chests

def get_path(keyring, locked_chests, path = []):
    # Try each key from keyring.
    for key in set(keyring):
        for chest in locked_chests[key]:
            # Add chest to path
            new_path = path + [chest.id]
            #print(new_path)
            # "Unlock" chest i.e. remove chest from dict.
            remaining_chests = unlock(key, chest, locked_chests)
            # Have all chests been unlocked yet?
            if not count(remaining_chests):
                return new_path # We are done
            else:
                # Get keys from chest
                new_keyring = keyring + chest.content
                # Remove used key from keyring
                new_keyring.remove(key)
                finished_path = get_path(new_keyring, remaining_chests, new_path)
                if finished_path:
                    return finished_path

def enough_keys(keyring, all_chests):
    required = []
    available = []
    available.extend(keyring)
    for key_type, matching_chests in all_chests.items():
        required.extend([key_type for chest in matching_chests])
        for chest in matching_chests:
            available.extend(chest.content)
    count_req = Counter(required)
    count_avail = Counter(available)
    return all(avail >= req for req in count_req for avail in count_avail)


def solve(keyring, locked_chests):
    if enough_keys(keyring, locked_chests):
        path = get_path(keyring, locked_chests)
        if path:
            return " ".join(str(chest) for chest in path)
    return "IMPOSSIBLE"


def main():
  for case, keys, locked_chests in get_data():
    print("Case #{}: {}".format(case, solve(keys, locked_chests)))

if __name__ == "__main__":
  main()

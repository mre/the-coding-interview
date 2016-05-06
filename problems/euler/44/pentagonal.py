from itertools import takewhile, combinations

def pentagonal_generator():
  n = 1
  while True:
    yield n*(3*n-1)/2
    n = n + 1

seen = set()

first_pentagonals = set(takewhile(lambda p: p < 100000000, pentagonal_generator()))

for pj, pk in combinations(first_pentagonals, 2):
  if pk + pj in first_pentagonals and pk - pj in first_pentagonals:
    print pj, pk, pk - pj

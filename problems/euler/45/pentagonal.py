from itertools import takewhile, combinations

def triangle_generator(start):
  n = 1
  while True:
    num = n*(n+1)/2
    if num >= start:
      yield num
    n = n + 1

def pentagonal_generator(start):
  n = 1
  while True:
    num = n*(3*n-1)/2
    if num >= start:
      yield num
    n = n + 1

def hexagonal_generator(start):
  n = 1
  while True:
    num = n*(2*n-1)
    if num >= start:
      yield num
    n = n + 1

start = 40756
tg = triangle_generator(start)
pg = pentagonal_generator(start)
hg = hexagonal_generator(start)

p = pg.next()
t = tg.next()

for h in hg:
  while p < h:
    p = pg.next()
  if p != h:
    continue
  while t < h:
    t = tg.next()
  if t == h:
    print h

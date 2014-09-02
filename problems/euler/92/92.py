def squares(n):
  return sum(int(i)**2 for i in str(n))


class memoize(dict):
  def __init__(self, func):
    self.func = func

  def __call__(self, *args):
    return self[args]

  def __missing__(self, key):
    result = self[key] = self.func(*key)
    return result


@memoize
def terminator(n):
  if n == 1 or n == 89:
    return n
  return terminator(squares(n))



results = [terminator(t) for t in range(10)]
print results


print sum(t for t in map(terminator, range(10)))




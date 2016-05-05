from math import sqrt, ceil
from collections import defaultdict
import operator

def generate_triangles_upto(max_perimeter):
  """
  Use Euclid's Formula to calculate the sides a, b, c of
  all right triangles up to a certain perimeter.

  a = m**2 - n**2
  b = 2*m*n
  c = m**2 + n**2

  with m > n

  perimeter = a + b + c 
  = m**2 - n**2 + 2mn + m**2 + n**2
  ~ 4m**2
  """
  triangles = defaultdict(set)
  max_value = int(ceil(sqrt(max_perimeter/2)))
  for m in range(1, max_value):
    for n in range(1, m):
      a = m**2 - n**2
      b = 2*m*n
      c = m**2 + n**2
      k = 1
      while k*a+k*b+k*c <= max_perimeter:
        triangles[k*a+k*b+k*c].add(tuple(sorted([k*a,k*b,k*c])))
        k = k + 1
  return triangles

triangles = generate_triangles_upto(1000).items()
print sorted([(k, len(v)) for k, v in triangles], key=operator.itemgetter(1))

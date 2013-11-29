def indizes_of(n, l):
  indizes = []
  for i, element in enumerate(l):
    if element == n:
      indizes.append(i)
  return indizes


def indizes_of_2(n, l):
  indizes = []
  i = 0
  try:
    while True:
      if l[i] == n:
        indizes.append(i)
      i += 1
  except:
    return indizes

field = [2,5,7,8,9,65,4,3,23,2,1,2,34,4,3,3,3,1,3,5,76,2]
print indizes_of(3, field)
print indizes_of_2(3, field)

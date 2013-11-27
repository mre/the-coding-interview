def merge(left, right):
  result = []
  while left and right:
    print left, right
    if left[0] < right[0]:
      result.append(left.pop())
    else:
      result.append(right.pop())
  # Add remaining elements
  result.extend(left)
  result.extend(right)
  return result

def mergesort(l):
  if len(l) < 2:
    # Already sorted
    return l
  # Divide...
  middle = len(l) / 2
  left = mergesort(l[:middle])
  right = mergesort(l[middle:])
  # ...and merge
  return merge(left, right)

print mergesort([4,6,8,5,2,1])

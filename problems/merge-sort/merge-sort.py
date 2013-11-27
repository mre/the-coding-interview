def merge(left, right):
  result = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  # Append remaining elements
  result.extend(left[i:])
  result.extend(right[j:])
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

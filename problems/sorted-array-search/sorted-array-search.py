def index_sorted(i, arr, start=0, stop=-1):
    if stop < start:
        stop = len(arr)
    if stop - start < 1:
        return None
    middle = int((stop-start)/2)
    elem = arr[middle]
    if elem == i:
        return middle
    if i < elem:
        return index_sorted(i, arr, start, middle)
    else:
        # i > elem
        return index_sorted(i, arr, middle+1, stop)

print index_sorted(3, [1,2,3,4,5,6,7,8,9])
print index_sorted(1, [1,2,3,4,5,6,7,8,9])
print index_sorted(1, [3,2,3,4,5,6,7,8,9])
print index_sorted(3, [0,3])
print index_sorted(3, [])

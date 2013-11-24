def kth_largest_naive(l, k):
    l.sort()
    return l[k-1]

def kth_largest(l, k):
    """
    Shorthand Quicksort
    Runtime: O(n * log n)
    """
    # kth largest element
    # is k-1th element in output
    k = k-1
    middle = len(l)/2
    pivot = l[middle]
    smaller = [i for i in l if i < pivot]
    if k < len(smaller):
        return kth_largest(smaller, k)
    equal  =  [i for i in l if i == pivot]
    if k < len(smaller) + len(equal):
        return pivot
    larger =  [i for i in l if i > pivot]
    return kth_largest(larger, k - len(smaller) - len(equal))


print kth_largest_naive([3, 1, 2, 1, 4], 3)
print kth_largest([3, 1, 2, 1, 4], 3)

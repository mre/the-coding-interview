def pairs_brute(k, arr):
    """
    Runtime: O(n^2)
    """
    if len(arr) < 2:
        return []
    pairs = []
    for i, n1 in enumerate(arr):
        for n2 in arr[i+1:]:
            if n1 + n2 == k:
                pairs.append([n1,n2])
    return pairs

def pairs_sort(k, arr):
    """
    Runtime: O(n^2)
    By sorting, we can avoid some unnecessary comparisons.
    """
    if len(arr) < 2:
        return []
    pairs = []
    arr.sort()
    for i, n1 in enumerate(arr):
        for n2 in arr[i+1:]:
            if n1 + n2 > k:
                # All other pairs will
                # be bigger than k. Stop.
                break
            if n1 + n2 == k:
                pairs.append([n1,n2])
    return pairs

def pairs(k, arr):
    """
    Runtime: O(n * log n)
    After sorting, we can iterate through the
    list from both sides in O(n) to find the pairs.
    """
    arr.sort()
    if len(arr) < 2:
        return []
    pairs = []
    start = 0
    end = len(arr)-1
    while (start < end):
        n1 = arr[start]
        n2 = arr[end]
        pair = n1 + n2
        if pair < k:
            start += 1
        if pair > k:
            end -= 1
        if pair == k:
            pairs.append([n1,n2])
            start += 1
    return pairs


def pairs_lin(k, arr):
    """
    Runtime: O(n)
    Adapted from: 
    ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum
    """
    if len(arr) < 2:
        return []
    output = seen = []
    for n in arr:
        partner = k - n
        if partner in seen:
            output.append([n, partner])
        else:
            seen.append(n)
    return output


print pairs_lin(10, [3, 4, 5, 6, 7]) # [[6, 4], [7, 3]]
print pairs_lin(8, [3, 4, 5, 4, 4]) # [[3, 5], [4, 4], [4, 4], [4, 4]]
print pairs_lin(8, [4]) # []
print pairs_lin(0, [4,-4]) # [[-4,4]]

def bubblesort(l):
    """
    Runtime: O(n^2)
    """
    last = len(l)-1
    for i in range(last):
        for j in range(i+1, last):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

print bubblesort([8,2,4,7,9,0,1,4,5,7,8,9])
print bubblesort([])
print bubblesort([1])
print bubblesort([1,3])

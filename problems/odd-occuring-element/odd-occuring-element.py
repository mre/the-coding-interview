def odd_occuring_element(l):
    result = 0
    for i in l:
        result ^= i
    return result

print odd_occuring_element([1,1,2,2,3])
print odd_occuring_element([1,2,1,2,2])

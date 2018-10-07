def missing_number(l):
    non_missing = sum(range(1,len(l)+2))
    missing = sum(l)
    return non_missing - missing

print missing_number([1,2,3,4,6])

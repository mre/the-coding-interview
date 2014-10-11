def combinations(start, stop):
    for a in range(start, stop+1):
        for b in range(start, stop+1):
            yield a**b

# Test
#print len(set(combinations(2,5))) # 15
print len(set(combinations(2,100)))

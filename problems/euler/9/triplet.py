maximum = 1000
for a in range(maximum,1,-1):
    for b in range(maximum-a,1,-1):
        for c in range(maximum-a-b,1,-1):
            if a + b + c != 1000:
                continue
            if a**2+b**2 == c**2:
                print a*b*c

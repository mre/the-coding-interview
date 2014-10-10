## 1
#> 2
## 3  5  7  9
#> 10 12 14 16
## 13 17 21 25
#> 18 20 22 24
## 31 37 43 49

"""
1 1
3 9
5 25
7 49
9 81
...
1001 1002001
"""

def stepper(start, step, duplicates):
    # 2 2 2 2 4 4 4 4 6 6 6 6 8 8 8 8 8
    while True:
        for d in range(duplicates):
            yield start
        start += step

def diag_gen_upto(n):
    diag = 1
    for increment in stepper(2,2,4):
        if diag > n:
            break
        yield diag
        diag += increment

def spiral_diagonals(n):
    return [d for d in diag_gen_upto(n**2)]
    
# Tests
print spiral_diagonals(3) # 1,3,5,7,9
print spiral_diagonals(5) # 1,3,...,21,25

print sum(spiral_diagonals(1001))

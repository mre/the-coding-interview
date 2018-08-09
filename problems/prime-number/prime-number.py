from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    elif n in [2, 3]:
        return True 
    # To understand the statement below, please visit https://github.com/mre/the-coding-interview/pull/33   
    elif n % 6 not in [1, 5]:
        return False
    for i in range(3, int(sqrt(n))+1, 2): # change range to xrange for python2
        if n % i == 0:
            return False
    return True

print(is_prime(13))

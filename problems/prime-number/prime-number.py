from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    elif n % 6 not in [1, 5]:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1, 2): # change xrange to range for Python3
        if n % i == 0:
            return False
    return True

print(is_prime(13))

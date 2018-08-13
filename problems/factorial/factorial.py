# Recursive factorial
def fac(n):
    return 1 if n == 1 else n * fac(n-1)

print(fac(3))  # 6
print(fac(33)) # 8683317618811886495518194401280000000

# Iterative factorial
def fac(n):
    res = i = 1
    while i <= n:
        res *= i
        i += 1
    return res

print(fac(3))  # 6
print(fac(33)) # 8683317618811886495518194401280000000

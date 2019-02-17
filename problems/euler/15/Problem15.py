from math import factorial as f

t=int(input())
for i in range(t):
    m, n = [int(j) for j in input().split(" ")]
    print((f(m + n) // (f(m) * f(n))) % 1000000007)

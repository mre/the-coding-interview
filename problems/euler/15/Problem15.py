from math import factorial as f

#We have to just select paths.
t=int(input())
for i in range(t):
    m, n = [int(j) for j in input().split(" ")]
    print((f(m + n) // (f(m) * f(n))) % 1000000007)

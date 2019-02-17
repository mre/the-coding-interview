t=int(input())
for i in range(t):
    n=int(input())
    k=2**n
    s=0
    while k!=0:
        r=k%10
        s=s+r
        k=k//10
    print(s)

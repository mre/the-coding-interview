n=int(input())
l=[]
s=0
for i in range(0,n):
    l.append(int(input()))
    s=s+l[i]
st=str(s)
print(st[:10])

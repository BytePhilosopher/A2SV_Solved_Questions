n,k=map(int,input().split())
a=list(map(int,input().split()))

p=[]
for i in range(n):
    p.append((a[i],i+1))

p.sort()

l=[]
cur=0

for d,idx in p:
    if cur+d<=k:
        cur+=d
        l.append(idx)
    else:
        break
print(len(l))
if l:
    print(*l)
else:
    print()
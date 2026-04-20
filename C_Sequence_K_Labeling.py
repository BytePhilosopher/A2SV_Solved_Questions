n,k=map(int,input().split())
a=list(map(int,input().split()))

if n<k:
    print("NO")
    exit(0)

item=[]
for i in range(n):
    item.append((a[i],i))
item.sort()


cur=1
for i in range(1,n):
    if item[i][0]==item[i-1][0]:
        cur+=1
    else:
        cur=1
    if cur>k:
        print("NO")
        exit(0)
res=[0]*n
for i in range(n):
    lab=(i%k)+1
    org=item[i][1]
    res[org]=lab
print("YES")
print(*res)

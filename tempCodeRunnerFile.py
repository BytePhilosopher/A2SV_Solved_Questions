n,s = map(int, input().split())
a=list(map(int, input().split()))
total,count=0,0
ans=float('inf')

for left in range(n):
    total+=a[left]
    while total>s:
        total-=a[left-count]
        ans=min(ans, count)
        count+=1


print(ans if ans!=float('inf') else 0)
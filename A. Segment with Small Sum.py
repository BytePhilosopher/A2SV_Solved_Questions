n,s = map(int, input().split())
a=list(map(int, input().split()))
total,left=0,0
ans=float('inf')

for right in range(n):
    total+=a[right]

    while total>s:
        total-=a[left]
        ans=min(ans, right-left+1)
        left+=1


print(ans if ans!=float('inf') else 0)
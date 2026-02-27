from collections import defaultdict


n,m = map(int, input().split())
a=list(map(int, input().split()))
count=defaultdict(int)
ans,left=0,0
for right in range(n):
    count[a[right]]+=1
    while len(count)>m:
        count[a[left]]-=1
        if count[a[left]]==0:
            del count[a[left]]
        left+=1
   
    ans+=right-left+1
print(ans)
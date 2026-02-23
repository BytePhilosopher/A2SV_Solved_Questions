n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=[]
left,right=0,0
while left<n and right<m:
    if a[left]<=b[right]:
        ans.append(a[left])
        left+=1
    else:
        ans.append(b[right])
        right+=1
ans.extend(a[left:])
ans.extend(b[right:])
print(*ans)
n,m = map(int, input().split())
nums=list(map(int, input().split()))
total=0
ans=0
tempsum=0
for right in range(n):
    left=0
    total+=nums[right]
    while total>m and left<=right:
        total-=nums[left]
        tempsum+=nums[left]
        ans+=1
        left+=1
    total+=tempsum
    tempsum=0


print(ans)
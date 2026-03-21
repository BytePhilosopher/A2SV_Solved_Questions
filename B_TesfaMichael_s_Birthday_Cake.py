n,k=map(int,input().split())
s=input()
ar=sorted([ord(c)-96 for c in s])

l=-100
count=0
ans=0

for x in ar:
    if x>=l+2:
        ans+=x
        l=x
        count+=1


    if count==k:
        break
if count<k:
    print(-1)
else: print(ans)



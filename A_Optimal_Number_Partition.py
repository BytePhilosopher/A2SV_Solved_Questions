n=int(input())
a=list(map(int,input().split()))
a.sort()
res=0
for i in range(n//2):
    ans=a[i]+a[n-1-i]
    res+=(ans**2)
print(res)


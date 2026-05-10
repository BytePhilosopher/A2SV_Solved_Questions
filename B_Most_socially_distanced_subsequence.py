t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    ans=[]
    for i in range(n):
        if i==0 or i==n-1:
            ans.append(a[i])
        else:
            if a[i]>a[i-1] and a[i]>a[i+1]:
                ans.append(a[i])
            elif a[i]<a[i-1] and a[i]<a[i+1]:
                ans.append(a[i])
    print(len(ans))
    print(*ans)

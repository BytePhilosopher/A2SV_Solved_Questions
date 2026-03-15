t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(map(int,input().split()))

    # a.sort()
    ans=0
    l=0

    for r in range(n):
        while (a[r] -a[l]) >(n-1):
            l+=1

        ans=max(ans, r-l+1)


    print(ans)
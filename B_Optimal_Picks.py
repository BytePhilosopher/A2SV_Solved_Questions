t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))

    a.sort(reverse=True)
    tot=0

    for i in range(0,n-1,2):
        eve=a[i]
        noah=a[i+1]

        gap=eve-noah

        inc=min(k,gap)

        noah+=inc
        k-=inc
        tot+= (eve-noah)


    if n%2==1:
        tot+=a[-1]

    print(tot)
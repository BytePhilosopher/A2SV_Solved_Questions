t=int(input())
for _ in range(t):
    n,m=map(int, input().split())

    tot=n*m

    g=[]
    for _ in range(n):
        g.extend(input().split())

    if tot==1:
        print(-1)
        continue

    sh=g[-1:] + g[:-1]


    for i in range(0, tot,m):
        print(*sh[i:i+m])
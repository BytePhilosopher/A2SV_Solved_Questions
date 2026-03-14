t=int(input())
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))

    group={}
    for i in range(n):
        size=s[i]
        if size not in group:
            group[size]=[]
        group[size].append(i)

    ans=[0]*n
    p=True

    for size in group:
        idx=group[size]

        if len(idx)==1:
            p=False
            break

        for j in range(len(idx)):
            ans[idx[j]]=idx[(j+1)% len(idx)]+1


    if not p:
        print(-1)
    else:
        print(*ans)
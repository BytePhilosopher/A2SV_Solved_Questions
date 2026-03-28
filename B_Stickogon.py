from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input().strip())
    a=list(map(int,input().split()))
    cm=Counter(a)

    ans=0
    for f in cm.values():
        ans+=f//3
    print(ans)
    
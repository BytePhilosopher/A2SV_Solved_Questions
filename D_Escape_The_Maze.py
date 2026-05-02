from collections import deque

def ans():
    l=input().strip()
    while l==" ":
        l=input().strip()
    n,k=map(int,input().split())
    friend=list(map(int,input().split()))

    adj=[[] for _ in range(n+1)]

    for _ in range(n-1):
        u, v= map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dist=[-1]* (n+1)
    q_f=deque()

    for x in friend:
        dist[x]=0
        q_f.append(x)

    while q_f:
        u=q_f.popleft()
        for v in adj[u]:
            if dist[v]==-1:
                dist[v]= dist[u]+1
                q_f.append(v)
    dist_v=[-1]*(n+1)
    dist_v[1]=0
    q_v=deque([1])

    while q_v:
        u=q_v.popleft()

        if u!=1 and len(adj[u])==1:
            print("YES")
            return
        
        for v in adj[u]:
            if dist_v[v]==-1 and dist_v[u]+1< dist[v]:
                dist_v[v]=dist_v[u]+1
                q_v.append(v)
    print("NO")

t= int(input())
for _ in range(t):
    ans()
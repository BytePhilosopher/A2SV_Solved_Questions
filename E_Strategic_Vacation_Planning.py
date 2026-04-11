n,x=map(int,input().split())
s=[]
e=[]
for _ in range(n):
    l,r,cost=map(int,input().split())
    leng=r-l+1
    voucher=[l,r,cost,leng]
    s.append(voucher)
    e.append(voucher[:])

INF=10**18
min_cost=[INF]*(x+1)
s.sort(key=lambda v:v[0])
e.sort(key=lambda v:v[1])

ans=INF
end=0
for i in range(n):
    l,r,cost,leng=s[i]

    while end<n and e[end][1]<l:
        d=e[end][3]
        if d<x:
            min_cost[d]=min(min_cost[d],e[end][2])
        end+=1
    target_len=x-leng
    if 0<target_len<x and min_cost[target_len]!=INF:
        ans=min(ans,cost+min_cost[target_len])

if ans>=INF:
    print(-1)
else:
    print(ans)

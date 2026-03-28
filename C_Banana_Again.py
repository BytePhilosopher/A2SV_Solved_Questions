n=int(input())
a=list(map(int,input().split()))
tot=sum(a)
def dfs(i,cur):
    if i==n:
        return abs(tot-2 * cur)
    
    t=dfs(i+1,cur+a[i])
    s=dfs(i+1,cur)

    return min(t,s)
print(dfs(0,0))
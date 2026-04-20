def getmax(a,n):
    present=[False]*(n+1)
    for x in a:
        if x<=n:
            present[x]=True
    for i in range(n+1):
        if not present[i]:
            return i
        
def is_sorted(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    ans = []
    while not is_sorted(a):
        mex = getmax(a, n)
        if mex < n:
            a[mex] = mex
            ans.append(mex + 1)
        else:
            for i in range(n):
                if a[i] != i:
                    a[i] = mex
                    ans.append(i + 1)
                    break
    print(len(ans))
    print(*ans)



   
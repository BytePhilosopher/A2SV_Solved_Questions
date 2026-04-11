t=int(input())
for _ in range(t):
    n,h=map(int,input().split())
    tot=0

    for _ in range(n):
        a,b=map(int,input().split())
        tot+=max(a,b)
        
    if tot>=h:
        print("YES")
        
    else:
        print("NO")

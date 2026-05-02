t= int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    _max=(n+m-1)//m
    part=n-_max
    if k>=part:
        print("NO")
    else:
        print("YES")
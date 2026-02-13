
t=int(input())


for _ in range(t):
    n=int(input())
    s=input().strip()

    res=float('inf') 
    for i in range(n):
        right=n-1
        if s[i]=="a":
            while right>i:
                if s[right]=="a":
                    res=min(res,right-i+1)
                right-=1
    if res==float('inf'):
        print(-1)
    else:
        print(res)


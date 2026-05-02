t=int(input())

for _ in range(t):
    n=int(input().strip())
    p=list(map(int, input().split()))

    flag=False
    for i in range(n):
        f=i+1
        best=p[i]

        if p[best-1]==f:
            print(2)
            flag=True
            break
    if not flag: 
        print(3)

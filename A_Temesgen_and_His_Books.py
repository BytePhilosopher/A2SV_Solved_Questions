t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    last=a[-1]
    _max=max(a[:-1])
    print(_max+last)

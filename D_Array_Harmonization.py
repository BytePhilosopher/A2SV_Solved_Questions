t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a.sort
    b.sort()

    a_=[1]+a
    a_.sort()

    match=0
    ptr=0
    for bval in b:
        if ptr<n and a_[ptr]<bval:
            match+=1
            ptr+=1

    res=(n-match)*m
    print(res)

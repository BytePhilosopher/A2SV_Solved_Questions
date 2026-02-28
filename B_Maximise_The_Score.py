t=int(input())

for _ in range(t):
    n=int(input())
    num=list(map(int,input().split()))

    num.sort()

    total=sum(num[::2])

    print(total)

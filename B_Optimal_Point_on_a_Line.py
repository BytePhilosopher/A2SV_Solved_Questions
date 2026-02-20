n=int(input())
xi=list(map(int,input().split()))
xi.sort()



if n%2==0:
    print((xi[(n//2)-1]))
else:
    print(xi[n//2])

n,b=map(int, input().split())
arr=list(map(int,input().split()))

cost=[]
e=0
o=0

for i in range(n-1):
    if arr[i]%2==0:
        e+=1
    else:
        o+=1

    if e==o:
        cut=abs(arr[i]-arr[i+1])
        cost.append(cut)

    cost.sort()

    cutted=0
    money=0

    for co in cost:
        if money+co<=b:
            money+=co
            cutted+=1

        else:
            break
print(cutted)
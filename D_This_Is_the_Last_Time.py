t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    casino=[]

    for _ in range(n):
        casino.append(list(map(int,input().split())))
    
    casino.sort(key=lambda x: (x[0]))


    for i in range(n):
        

        if k in range(casino[i][0], casino[i][1]+1):
            k=max(k, casino[i][2])



    print(k)



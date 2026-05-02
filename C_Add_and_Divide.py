t=int(input())
for _ in range(t):
    ao,bo=map(int,input().split())

    min_op=float('inf')

    for c in range(35):
        b=bo+c

        if b<2:
            continue
        
        count=0
        temp=ao

        while temp>0:
            temp//=b
            count+=1
        total=count+c
        min_op=min(min_op,total)

    print(min_op)
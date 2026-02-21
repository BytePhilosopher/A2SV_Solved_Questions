n,k=map(int,input().split())
num=list(map(int,input().split()))


temp=[[0] for _ in range(k)]
index=n-1

minimum=num[0]

for i in range(k-1,-1,-1):
    if i==0:
        temp[i]=num[:index+1]
        break
    temp[i]=[num[index]]
    j=index-1


    while j>=0:
        if (temp[i][0])-(num[j])<minimum :
            temp[i].append(num[j])
            index-=1
        else:
            break
        j-=1
    index-=1

cost=0
for i in range(k):
    if len(temp[i])>1:
        cost+=abs(temp[i][-1]-temp[i][0])
print(cost)



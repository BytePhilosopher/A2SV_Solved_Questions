n,m=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
res=[]


ans=0
for i in range(m):
    while  ans<n and num2[i]>num1[ans] :
            ans+=1

    res.append(ans)


print(*res)


          
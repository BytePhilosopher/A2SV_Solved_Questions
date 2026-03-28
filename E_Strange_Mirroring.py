t=int(input())
for _ in range(t):
    s=input()
    q=int(input())
    k=list(map(int,input().split()))
 
    n=len(s)
    res=[]
 
    for i in k:#10**18
        t=0
        l=n
        temp_i=i-1
        while l<=temp_i:
            l*=2
 
        while temp_i>=n:
            h=l//2
            if temp_i>=h:
                temp_i-=h
                t+=1
            l=h
 
        ch=s[temp_i]
        if t%2==1:
            if ch.islower():
                ch=ch.upper()
            else:
               ch=ch.lower()
        res.append(ch)
 
    print(*res)
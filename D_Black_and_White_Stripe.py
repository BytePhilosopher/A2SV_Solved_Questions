t=int(input())

for _ in range(t):
    n,k=map(int,input().split())
    s=input().strip()
    


    count=s[:k].count("W")
    ans=count

    for right in range(k,n):
        if s[right]=="W":
            count+=1

        if s[right-k]=="W":
            count-=1

        ans=min(count, ans)
    print(ans)


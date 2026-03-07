t=int(input())
for _ in range(t):
    n=int(input())
    d=list(input())

    while d and int(d[-1])%2==0:
        d.pop()

    if not d:
        print(-1)
        continue

    

    tot=sum(int(c) for c in d)
    
    
    if tot%2!=0:
        rem=False
        
        for i in range(len(d)-1):
            if int(d[i])%2==1:
                d.pop(i)
                rem=True
                break
        if not rem:
            print(-1)
            continue
    res="".join(d).lstrip("0")
    if res:
        print(res)
        
    else:
        print(-1)

    




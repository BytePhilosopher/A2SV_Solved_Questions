t=int(input())


for _ in range(t):
    w=input().strip()
    max_p=int(input())

    tot=0
    count=[0]*27

    for ch in w:
        val=ord(ch)- ord('a') + 1
        tot+=val
        count[val]+=1


    for val in range(26,0,-1):
        if tot<=max_p:
            break

        need=tot-max_p
       
        act_rem=min(count[val],((need+val-1)//val))

        tot-= act_rem* val
        count[val]-=act_rem


    res=[]
    for ch in w:
        val=ord(ch)-ord('a')+1
        if count[val]>0:
            res.append(ch)
            count[val]-=1

    res="".join(res)
    print(res)
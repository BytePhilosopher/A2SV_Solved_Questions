t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))

    w,cur,left=0,0,0

    for right in range(n):
        cur+=a[right]

        while cur>r:
            cur-=a[left]
            left+=1

        
        if cur in range(l,r+1):
            w+=1
            cur=0
            left=right+1
    print(w)
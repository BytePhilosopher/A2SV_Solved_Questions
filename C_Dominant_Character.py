from collections import Counter

t=int(input())

for _ in range(t):
    n=int(input())
    s=input().strip()
        
    list_count=list(s)
    right=len(list_count)-1
    leftFlage=False


    for left in range(len(s)):

        if s[left]!="a" and leftFlage!=True:
            list_count.pop(left)
            right-=1
        elif s[left]=="a":
            leftFlage=True

        count=Counter(list_count)
        if count.get("a",0)<=(count.get("b",0)+count.get("c",0)):
            list_count.pop()
            right-=1

        if left+2==right:
            break
    
    if count.get("a",0)<(count.get("b",0)+count.get("c",0)):
        print(-1)
    else:   
        print(right+1)


from collections import Counter


t=int(input())
for _ in range(t):
    s = input()
    count=Counter(s)
    res=[]

    for key,val in count.items():
        if val%2!=0:
           res.append(key)
    res.sort()
    print("".join(res))

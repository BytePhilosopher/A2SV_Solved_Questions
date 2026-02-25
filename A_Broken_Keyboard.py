
t=int(input())
for _ in range(t):
    s = input()
    ans=set()

    ptr=0
    while ptr<len(s):
        i=ptr
        check=0
        while i<len(s) and s[i]==s[ptr]:
            check+=1
            i+=1
        if check%2!=0:
            ans.add(s[ptr])
        ptr=i
    ans=sorted(ans)

    print("".join(ans))


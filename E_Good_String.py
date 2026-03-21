n=int(input())
s=input()

res=[]

for c in s:
    if len(res)%2==0:
        res.append(c)
    else:
        if c!=res[-1]:
            res.append(c)

if len(res)%2!=0:
    res.pop()

print(n-len(res))
print("".join(res))


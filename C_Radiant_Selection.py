import math
t=int(input())
for _ in range(t):
    k=int(input())
    res=k+int(math.isqrt(k))

    if res-int(math.isqrt(res))<k:
         res+=1
    print(res)
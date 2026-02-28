
from typing import Counter
t=int(input())
for _ in range(t):
    s = input().strip()
    n=len(s)

    h=s[:n//2]

    if len(set(h))>1:
        print("YES")
    else:
        print("NO")



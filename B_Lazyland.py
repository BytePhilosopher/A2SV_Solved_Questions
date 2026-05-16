from collections import defaultdict
from heapq import heappush, heappop
import heapq
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

jc=defaultdict(list)


for i in range(n):
    jc[a[i]].append(b[i])

free=[]
uni=len(jc)

for i in jc.values():
    if len(i)>1:
        i.sort()
        for j in i[:-1]:
            heapq.heappush(free,j)
 
min_tot=0
job=k-uni
for i in range(job):
    if free:
        min_tot+=heapq.heappop(free)


print(min_tot)
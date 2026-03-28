# class F:
#     def _init_(self,n):
#         self.n=n
#         self.tree=[0]*(n+1)
#     def x(self,i,v):
#         while i<=self.n:
#             self.tree[i]+=v
#             i+=i
#     def q(self,i):
#         s=0
#         while i>0:
#             s+=self.tree[i]
#             i-=1
#         return s

t=int(input())
for _ in range(t):
    n=int(input())
    people=[]

    for _ in range(n):
        a,b=map(int,input().split())
        people.append((a,b))

    count=0
    for i in range(n):
        for j in range(i+1,n):
            a1,b1=people[i]
            a2,b2=people[j]

            if (a1<a2 and b1>b2) or (a2<a1 and b2>b1):
                count+=1
    print(count)
    
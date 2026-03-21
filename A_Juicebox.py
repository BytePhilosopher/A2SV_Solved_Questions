t=int(input())

for _ in range(t):
    n,k=map(int, input().split())

    br=[0]*(k+1)

    for _ in range(k):
        b,c=map(int,input().split())
        br[b]+=c

    tot=sorted((v for v in br if v>0), reverse=True)

    print(sum(tot[:n]))
  


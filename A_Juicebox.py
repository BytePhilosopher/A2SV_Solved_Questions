        t=int(input())

        for _ in range(t):
            n,k=map(int, input().split())

            br={}

            for _ in range(k):
                b,c=map(int,input().split())
                br[b]=br.get(b,0)+c

            tot=sorted(br.values(), reverse=True)

            print(sum(tot[:n]))
            br.clear()


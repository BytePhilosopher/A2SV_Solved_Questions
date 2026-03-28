class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
    
        def comb(cur,i):
            if len(cur)==k:
                ans.append(cur[:])
                return
            

            for j in range(i,n+1):
                cur.append(j)
                comb(cur,j+1)
                cur.pop()

        

        comb([],1)
        return ans 
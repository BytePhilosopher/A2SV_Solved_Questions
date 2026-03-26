class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
    
        def comb(cur,i):
            if len(cur)==k:
                ans.append(cur[:])
                return
            
            if i>n:
                return

            cur.append(i)

            comb(cur,i+1)

            cur.pop()

            comb(cur, i+1)

        comb([],1)
        return ans 
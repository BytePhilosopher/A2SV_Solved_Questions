class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        #8,8,10,20,15
        combs = [0]*k
        n=len(cookies)
        max_=float('inf')
        

        def helper2(i):
            nonlocal max_,combs
            if i == n:
                max_=min(max_,max(combs))
                return

            if max_<=max(combs):
                return

            for j in range(k):
                combs[j]+=cookies[i]
                helper2(i + 1)
                combs[j]-=cookies[i]
            

        

        helper2(0)
        return max_
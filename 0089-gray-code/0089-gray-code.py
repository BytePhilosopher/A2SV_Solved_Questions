class Solution:
    def grayCode(self, n: int) -> List[int]:
        result=[]
        seen=set()

        def dfs(num):
            #base case
            if num in seen:
                return
                
            result.append(num)
            seen.add(num)
            for i in range(n):
                num = num ^ (1<<i)
                dfs(num)
                num = num ^ (1<<i)

                
        dfs(0)
        return result
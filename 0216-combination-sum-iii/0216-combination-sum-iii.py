class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def dfs(start,temp,total):
            #base case

            if len(temp)==k and total==n:
                result.append(temp[:])
                return

            if len(temp)==k or total>=n:
                return

            for num in range(start,10):
                if num+total >n:
                    break
                temp.append(num)
                dfs(num+1,temp,total+num)
                temp.pop() #backtrac to undo

            # dfs(num+1,temp,total)
            

        dfs(1,[],0)

        return result
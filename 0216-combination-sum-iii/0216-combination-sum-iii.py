class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def dfs(num,temp,total):
            #base case

            if len(temp)==k and total==n:
                result.append(temp[:])
                return

            if len(temp)==k or total>=n or num>9:
                return

            # for i in range(j,11):
            temp.append(num)
            dfs(num+1,temp,total+num)
            temp.pop() #backtrac to undo

            dfs(num+1,temp,total)
            

        dfs(1,[],0)

        return result
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]

        def dfs(start,total):
            #base case
            if total==target:
                result.append(current[:])
                return

            for index in range(start,len(candidates)):
                if total + candidates[index] <=target:
                    #pick
                    current.append(candidates[index])
                    #backtrack
                    dfs(index,total+candidates[index])
                    current.pop()
            
        dfs(0,0)
        return result

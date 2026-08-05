class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
        candidates.sort()

        def dfs(start,remain):
            #base case
            if remain==0:
                result.append(current[:])
                return

            for index in range(start,len(candidates)):
                if remain<candidates[index]:
                    break
                #pick
                current.append(candidates[index])
                #backtrack
                dfs(index,remain-candidates[index])
                current.pop()
            
        dfs(0,target)
        return result

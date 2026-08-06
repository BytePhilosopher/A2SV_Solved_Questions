class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        result=[]
        curset=[]
        candidates.sort()

        def backtrack(remain,start):

            if remain==0:
                result.append(curset[:])

            for index in range(start,len(candidates)):
                if remain < candidates[index]:
                    break

                curset.append(candidates[index])
                backtrack(remain-candidates[index],index)
                curset.pop()

        backtrack(target,0)
        return result

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
 
        def dfs(i,temp,cursum):
            # base case
            if cursum==target:
                result.append(temp[:])
                return

            if cursum>target:
                return

            for j in range(i,len(candidates)):

                if j>i and candidates[j]==candidates[j-1]:
                    continue

                if cursum + candidates[j] >target:
                    break
                temp.append(candidates[j])

                dfs(j+1,temp, cursum + candidates[j])
                temp.pop()

        dfs(0,[],0)


        return result
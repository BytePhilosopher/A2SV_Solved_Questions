class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        used=set()
        def dfs(i,temp,cursum):
            # base case
            if cursum==target:
                result.append(temp[:])
                return

            if cursum>target:
                return

            for j in range(i,len(candidates)):
                # if cursum + candidates[j] <=target and candidates[j] not in used :
                    # break
                # else:
                if j>i and candidates[j]==candidates[j-1]:
                    continue

                if cursum + candidates[j] >target:
                    break
                temp.append(candidates[j])
                # used.add(candidates[j])
                dfs(j+1,temp, cursum + candidates[j])
                temp.pop()
                    # used.remove(candidates[j])
        dfs(0,[],0)


        return result
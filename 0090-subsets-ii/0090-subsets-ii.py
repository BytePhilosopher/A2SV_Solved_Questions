class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result,curset=[],[]

        def dfs(index):

            #base case
            
            result.append(curset[:])

            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                curset.append(nums[i])
                dfs(i+1)
                curset.pop()
                


        dfs(0)
        return result
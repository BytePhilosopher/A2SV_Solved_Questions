class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subset=set()

        def dfs(i, curset):
            used = set()
            if len(curset)>=2:
                subset.add(tuple(curset))
            if i>len(nums):
                return
            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue
                if curset and curset[-1] > nums[j]:
                    continue
                
                used.add(nums[j])
                curset.append(nums[j])
                dfs(j+1, curset)
                curset.pop()

        dfs(0,[])
        return [list(seq) for seq in subset]
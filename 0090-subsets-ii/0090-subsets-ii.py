class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset,curset=[],[]
        n=len(nums)
        nums.sort()

        def subsets(i,curset):
            if i>=len(nums):
                subset.append(curset[:])
                return
            curset.append(nums[i])
            subsets(i+1,curset)
            while i<len(nums)-1:
                if nums[i]!=nums[i+1]:
                    break
                else: i+=1
            curset.pop()
            subsets(i+1,curset)
            return

        subsets(0,curset)
        return subset
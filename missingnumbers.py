class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if 0 not in nums:
            return 0
        
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                continue
            else:
                return nums[i]+1
        return len(nums)
            
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index in range(len(nums)):
            for index2 in range(len(nums)):
                if index!=index2 and nums[index] + nums[index2]==target:
                    return [index,index2]

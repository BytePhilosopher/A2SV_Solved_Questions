class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker=0
        identify=0

        while seeker<len(nums):
            if nums[seeker]!=0:
                nums[seeker],nums[identify]=nums[identify],nums[seeker]
                identify+=1
            seeker+=1
 
                
                

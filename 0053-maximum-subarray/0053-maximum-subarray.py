class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]

        cur=0
        for num in nums:
            cur=max(cur,0)
            cur+=num
            maxsum=max(cur,maxsum)
            

        return maxsum


        
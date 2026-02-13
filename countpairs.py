class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for left in range(len(nums)-1):
            for right in range(left+1,len(nums)):
                if nums[left]==nums[right]:
                    if (left*right)%k==0:
                        count+=1
        return count

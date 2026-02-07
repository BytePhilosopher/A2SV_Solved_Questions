class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for idx,num in enumerate(nums):
            diff=target-num
            if diff in nums and idx!=nums.index(diff):
                ans.append(idx)
                ans.append(nums.index(diff))
                break
        return ans



        
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a, b):
            
            return str(a) + str(b) > str(b) + str(a)

        n = len(nums)
        
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if compare(nums[j], nums[max_idx]):
                    max_idx = j
            
           
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

   
        if nums[0] == 0:
            return "0"

        ans = ""
        for num in nums:
            ans += str(num)

        return ans

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        
        sum_diff = sum(nums) - n * (n + 1) // 2
        sq_diff = sum(x * x for x in nums) - n * (n + 1) * (2 * n + 1) // 6

        sum_both = sq_diff // sum_diff
        duplicate = (sum_diff + sum_both) // 2
        missing = sum_both - duplicate
        
        return [duplicate, missing]
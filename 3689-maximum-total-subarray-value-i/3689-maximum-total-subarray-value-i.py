class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx=max(nums)
        minx=min(nums)

        return (mx-minx)*k
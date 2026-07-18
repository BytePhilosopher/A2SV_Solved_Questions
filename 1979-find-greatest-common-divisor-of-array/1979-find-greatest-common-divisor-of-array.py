class Solution:
    def findGCD(self, nums: List[int]) -> int:
        _min=min(nums)
        _max=max(nums)

        import math

        return  math.gcd(_min, _max)
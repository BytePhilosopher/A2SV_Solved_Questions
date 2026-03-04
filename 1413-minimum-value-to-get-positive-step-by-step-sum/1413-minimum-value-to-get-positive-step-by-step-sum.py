class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #[ -3 , 2 , -3 , 4 , 2]
        # -3 -1  -4   0. 2

        #[1,-2,-3]
        #1 -1. -4

        #[2 , 3 , 5 ,-5 ,-1]
        #2. 5   10. 5   4
        _sum=min_val=0
        for num in nums:
            _sum=_sum+num
            min_val=min(_sum,min_val)

        return 1 - min_val
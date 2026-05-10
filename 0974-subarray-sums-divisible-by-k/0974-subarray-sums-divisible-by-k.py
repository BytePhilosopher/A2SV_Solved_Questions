class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        
        prefix = 0
        ans = 0
        
        for num in nums:
            prefix += num
            
            rem = prefix % k
            
           
            rem = (rem + k) % k
            
            ans += count[rem]
            
            count[rem] += 1
        
        return ans
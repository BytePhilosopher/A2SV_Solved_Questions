from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = defaultdict(int)
        pref[0] = 1 
        
        curr = 0
        count = 0
        
        for num in nums:
            curr += num
            
            if curr - goal in pref:
                count += pref[curr - goal]
            
            pref[curr] += 1
        
        return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # tot=0
        # count=0
        # pref=[tot:=tot+num for num in nums]

        # for i in range(len(nums)):
        #     j=0
        #     if pref[i]==k:
        #         count+=1
        #     while j<i:
        #         newsum=pref[i]-pref[j]
        #         if newsum==k:
        #             count+=1
        #         j+=1
        # return count
        pref = {0: 1}   # prefix_sum -> frequency
        total = 0
        count = 0
        
        for num in nums:
            total += num
            
            if total - k in pref:
                count += pref[total - k]
            
            pref[total] = pref.get(total, 0) + 1
        
        return count

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # tot=0
        # pref=[tot:= tot+num for num in nums]
        
        # for r in range(len(nums)):
        #     if (pref[r]%k==0) and r>=1:
        #         return True
        #     l=0
        #     while (r-l)>=2:
        #         if (pref[r]-pref[l]) % k==0:
        #             return True
        #         l+=1
        # return False
        pref={0:-1}
        total=0
        for i, num in enumerate(nums):
            total += num
            mod = total % k

            if mod in pref:
                if i-pref[mod] >= 2:
                    return True
            else:
                pref[mod]=i
        return False

        
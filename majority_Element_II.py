class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cm=Counter(nums)
        ans=[]
        n=len(nums)

        for key,val in cm.items():
            if val>int(n/3):
                ans.append(key)
            elif n<3 and val<2:
                return nums
            elif n<3 and val==2:
                return nums[0]
        return ans
        
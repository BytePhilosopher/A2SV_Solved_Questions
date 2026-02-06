class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cm=Counter(nums)
        for key,val in cm.items():
            if val==1:
                return key
        
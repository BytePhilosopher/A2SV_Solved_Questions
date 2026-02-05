class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans=[]
        cm=Counter(nums)
        for key,val in cm.items():
            if val==2:
                ans.append(key)
        return ans

        
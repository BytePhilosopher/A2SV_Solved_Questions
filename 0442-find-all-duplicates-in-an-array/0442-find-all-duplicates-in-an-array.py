class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        cm=Counter(nums)
        for key,val in cm.items():
            if val==2:
                ans.append(key)
        return ans


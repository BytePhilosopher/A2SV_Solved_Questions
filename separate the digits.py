class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]

        for n in nums:
            n=str(n)
            for s in list(n):
                ans.append(int(s))
        return ans
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        def findcount(mid):
            count=0
            for num in nums:
                if num<=mid:
                    count+=1
            return count
        left, right=1, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if findcount(mid)<= mid:
                left=mid+1
            else:
                right=mid-1
        return left
            

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        def findleft():
            l,r=0,len(nums)-1
            while(l<=r):
                mid=(l+r)//2
                if target<nums[mid]:
                    r=mid-1
                elif target>nums[mid]:
                    l=mid+1
                else:
                    ans[0]=mid
                    r=mid-1
        def findright():
            l,r=0,len(nums)-1
            while(l<=r):
                mid=(l+r)//2
                if target<nums[mid]:
                    r=mid-1
                elif target>nums[mid]:
                    l=mid+1
                else:
                    ans[1]=mid
                    l=mid+1
        findleft() 
        findright()
        return ans
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # midval=0
        def bs(l,r):
            mid=(l+r)//2
            if l>r:
                return -1
            if nums[mid]>target:
                return bs(l,mid-1)
            elif nums[mid]<target:
                return bs(mid+1,r)
            else:
                return mid
            # return -1
        
        return bs(0,len(nums)-1)

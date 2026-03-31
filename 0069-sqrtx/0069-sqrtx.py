class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        l,r=0,x
        while l<=r:
            mid=(l+r)//2
            if mid*mid <= x:
                ans=mid
                l=mid+1
            else:
                r=mid-1

        return ans
        
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def possible(mid):
            total=0
            for c in candies:
                total+=c//mid
            
            return total>=k
        l,r=1,sum(candies)//k
        while l<=r:
            mid=(l+r)//2
            if possible(mid):
                l=mid+1
            else:
                r=mid-1
        return r
            

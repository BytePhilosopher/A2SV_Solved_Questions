class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
    
        while l<=r:
            mid=(l+r)//2
            hours=0
            for k in piles:
                hours+=math.ceil(k/mid)

            if hours<=h:
                ans=mid
                r=mid-1
            elif hours>h:
                l=mid+1

        return l

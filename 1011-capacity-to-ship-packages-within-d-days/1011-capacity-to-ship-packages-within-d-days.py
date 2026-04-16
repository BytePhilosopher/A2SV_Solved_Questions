class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l,h=max(weights), sum(weights)
        while l<=h:
            mid=(l+h)//2
            shop=0
            d=1
            for w in weights:
                if shop+w>mid:
                    d+=1
                    shop=0
                shop+=w
            if d<=days:
                h=mid-1
            else:
                l=mid+1
        return l
                    


            
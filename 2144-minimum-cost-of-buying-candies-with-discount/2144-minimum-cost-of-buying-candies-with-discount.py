class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans=0
        while len(cost)>=3:
            ans+=cost.pop()
            ans+=cost.pop()
            cost.pop()
        if cost:
            ans+=sum(cost)
        return ans

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        total = 0
        end = n // 3
        indices=n-2

        for _ in range(end):
            total += piles[indices]
            indices-=2

        return total

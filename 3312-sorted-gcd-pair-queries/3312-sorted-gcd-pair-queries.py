from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[d] = how many numbers are divisible by d
        cnt = [0] * (mx + 1)
        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                cnt[d] += freq[m]

        # exact[d] = number of pairs with gcd exactly d
        exact = [0] * (mx + 1)
        for d in range(mx, 0, -1):
            c = cnt[d]
            exact[d] = c * (c - 1) // 2
            for m in range(d * 2, mx + 1, d):
                exact[d] -= exact[m]

        # prefix counts
        prefix = []
        values = []
        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans
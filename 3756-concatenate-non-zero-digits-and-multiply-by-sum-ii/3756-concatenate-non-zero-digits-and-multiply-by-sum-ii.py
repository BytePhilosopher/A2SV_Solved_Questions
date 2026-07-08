from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Prefix sum of non-zero digits in the original string
        prefSum = [0] * (n + 1)
        for i in range(n):
            prefSum[i + 1] = prefSum[i] + (int(s[i]) if s[i] != '0' else 0)

        # Compress non-zero digits
        digits = []
        pos = []
        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        k = len(digits)

        # Prefix concatenated values
        P = [0] * (k + 1)
        for i in range(k):
            P[i + 1] = (P[i] * 10 + digits[i]) % MOD

        # Powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # leftMap[i] = first non-zero digit at or after i
        leftMap = [-1] * n
        j = 0
        for i in range(n):
            while j < k and pos[j] < i:
                j += 1
            if j < k:
                leftMap[i] = j

        # rightMap[i] = last non-zero digit at or before i
        rightMap = [-1] * n
        j = k - 1
        for i in range(n - 1, -1, -1):
            while j >= 0 and pos[j] > i:
                j -= 1
            if j >= 0:
                rightMap[i] = j

        ans = []

        for l, r in queries:
            L = leftMap[l]
            R = rightMap[r]

            if L == -1 or R == -1 or L > R:
                ans.append(0)
                continue

            # Sum of non-zero digits in the substring
            digitSum = prefSum[r + 1] - prefSum[l]

            # Concatenated number modulo MOD
            length = R - L + 1
            x = (P[R + 1] - P[L] * pow10[length]) % MOD

            ans.append((x * digitSum) % MOD)

        return ans
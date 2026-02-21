class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=""
        count=Counter(s)

        for ch in order:
            if ch in s:
                ans+=ch*count[ch]

        for char in s:
            if char not in ans:
                ans+=char*count[char]

        return ans


            

        
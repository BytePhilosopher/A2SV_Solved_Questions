class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t=list(s)
        for ch in range(len(s)):
            idx=indices[ch]
            t[idx]=s[ch]
            print(t)


        return "".join(t)
        
class Solution:
    def maxScore(self, s: str) -> int:
        _sum=0
        pre=[_sum:=_sum+int(ch) for ch in s]
        ans=0

        for i in range(len(s)-1):
            temp=0
            temp=pre[-1]-pre[i] + s[:i+1].count('0')
            ans=max(ans,temp)
            print(temp)
        return ans
        
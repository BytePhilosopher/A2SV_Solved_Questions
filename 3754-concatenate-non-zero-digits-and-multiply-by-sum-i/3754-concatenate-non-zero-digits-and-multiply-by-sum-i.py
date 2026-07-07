class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        x=""
        nums=str(n)
        for num in nums:
            if num !="0":
                x+=num
                sum+=int(num)
        return int(x)*sum if sum!=0 else 0

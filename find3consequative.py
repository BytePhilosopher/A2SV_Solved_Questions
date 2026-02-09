class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n=int(num/3)
        if sum([n,n+1,n-1])==num:
            return [n-1,n,n+1]
        return []
        
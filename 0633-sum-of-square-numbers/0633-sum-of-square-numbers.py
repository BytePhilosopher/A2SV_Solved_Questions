class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        perfecto=int(sqrt(c))

        while perfecto>=0:
            left=c-pow(perfecto,2)
            lefto=int(sqrt(left))
            if pow(lefto,2)+ pow(perfecto,2)==c:
                return True
            perfecto-=1


       
        return False
        
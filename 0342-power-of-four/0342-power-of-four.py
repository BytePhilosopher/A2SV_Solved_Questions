class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count=0
        def powe(n):
          
            if n==1:
                return True
            elif n<1:
                return False
            
            return powe(n/4)

        x=powe(n)

        
        return x
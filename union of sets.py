class Solution:    
    def findUnion(self, a, b):
        # code here
        result=a+b
        result.sort()
        result=set(result)
        return result
                
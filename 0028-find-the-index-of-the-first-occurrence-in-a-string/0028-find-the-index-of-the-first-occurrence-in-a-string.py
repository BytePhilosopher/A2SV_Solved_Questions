class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range (len(haystack)-len(needle)+1):
            check=True
            for j,val in enumerate (needle):
                if haystack[j+i]!=val:
                    check=False
                    break
            if check:
                return i


        return -1
        
        

        
                
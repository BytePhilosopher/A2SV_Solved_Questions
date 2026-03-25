class Solution:
    def splitString(self, s: str) -> bool:
        path=[]
        n=len(s)


        def rec(path,i):
            if i==n:
                for r in range(1,len(path)):
                    if path[r]!=path[r-1]-1:
                        return False
                return len(path)>=2
            
            

            for c in range(i,len(s)):
                val = int(s[i : c + 1])
                path.append(val)

                if rec(path,c+1):
                    return True

                path.pop()

            return False

        
        return rec(path,0)
        
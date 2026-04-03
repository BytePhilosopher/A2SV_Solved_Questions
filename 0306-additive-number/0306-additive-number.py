class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        stack=[]
        n=len(num)
        def dfs(i):
            if i == n:
                return len(stack) >= 3
            
            for j in range(i, n):
                if num[i] == '0' and j > i:
                    break
                
                val = num[i:j+1]
                
                if len(stack) >= 2:
                    if int(val) < int(stack[-1]) + int(stack[-2]):
                        continue
                    elif int(val) > int(stack[-1]) + int(stack[-2]):
                        break
                
                stack.append(val)
                if dfs(j+1):
                    return True
                stack.pop()
            return False
        
        return dfs(0)
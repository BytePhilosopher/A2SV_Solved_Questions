class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        
        for char in s:
            if char != "]":
                stk.append(char)
            else:
                temp = ""
                while stk and stk[-1] != "[":
                    temp = stk.pop() +temp
           
                stk.pop()  
     
                mult = ""
                while stk and stk[-1].isdigit():
                    mult = stk.pop() + mult 
                mult = int(mult)
                
                
                stk.append(temp * mult)
        
        return "".join(stk)
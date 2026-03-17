class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        "(())()"
        stk=[0]
        count=0

        for ch in s:
            if ch!=")":
                stk.append(0)

            else :
                score=stk.pop()
                if score==0:
                    count=1
                else:
                    count=2* score
                stk[-1]+=count
                
        return stk[0]

                

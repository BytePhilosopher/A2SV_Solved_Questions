class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for si in s:
            if stk and si=="*":
                stk.pop()
            else:
                stk.append(si)

        return "".join(stk)

        
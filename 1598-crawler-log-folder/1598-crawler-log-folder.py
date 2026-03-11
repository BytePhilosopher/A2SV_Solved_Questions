class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk=[]
        for log in logs:
            if log=="../":
                if stk: stk.pop()
            elif log=="./":
                continue
            else: stk.append(log)
        print(stk)
        return len(stk)
        
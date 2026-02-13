class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter=Counter(s)
        t_counter=Counter(t)

        if s_counter==t_counter:
            return 0

        steps=0
        for k,val in s_counter.items():
            if val>t_counter[k]:
                steps+=val-t_counter[k]
            print(steps)

        return steps



        
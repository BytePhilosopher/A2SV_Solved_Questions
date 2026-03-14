class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt=defaultdict(int)
        res=0
        # [4 4 4 4 4 4]
        # 3  2. 1. 0 +4
        # [0 0 1 1 1]
        for key in answers:
            cnt[key]+=1

             
        print(cnt)
        for ans in cnt.keys():
            if ans==0:
                res+=cnt[0]
            elif cnt[ans]>ans:
                gp=(cnt[ans] + ans) // (ans + 1) 
                res+=gp * (ans+1)
            elif cnt[ans]<=ans:
                res+=ans+1

        return res
                
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        _sum={5:0,10:0,20:0}
        if bills[0]!=5:
            return False

        for bill in bills:
            if bill==5:
                _sum[5]+=1
            elif bill==10:
                if _sum[5]>=1:
                    _sum[5]-=1
                    _sum[10]+=1
                else:
                    return False
            elif bill==20:
                if _sum[5]>=1 and _sum[10]>=1:
                    _sum[5]-=1
                    _sum[10]-=1
                    _sum[20]+=1
                elif _sum[5]>=3:
                    _sum[5]-=3
                    _sum[20]+=1
                else:
                    return False

        return True
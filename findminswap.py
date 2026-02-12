class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n = len(s1)
        count = 0
        
        s1 = list(s1)
        s2 = list(s2)
        
        xy = 0
        yx = 0
        
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx += 1
        
        if (xy + yx) % 2 != 0:
            return -1
        
        count += xy // 2
        count += yx // 2
        
        if xy % 2 == 1:
            count += 2
        
        return count

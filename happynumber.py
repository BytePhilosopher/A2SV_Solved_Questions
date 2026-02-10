class Solution:
    def isHappy(self, n: int) -> bool:
        
        num=list(map(int,list(str(n))))
        sum=0
        seen=set()
        while True:
            sum=0
            for index in range(len(num)):
                sum+=num[index]*num[index]
            num=list(map(int,list(str(sum))))
            
            if sum not in seen:
                seen.add(sum)
            else:
                break

            if sum==1:
                return True
        

        
        return False
        
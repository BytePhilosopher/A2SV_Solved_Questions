class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness=0
        for num in range(num1,num2+1):
            num=str(num)
            if len(num)<3:
                continue
            else:
                for j in range(1,len(num)-1):
                    if num[j]<num[j-1] and num[j]< num[j+1]:
                        waviness+=1
                    
                    elif num[j]>num[j-1] and num[j]> num[j+1]:
                        waviness+=1

        return waviness
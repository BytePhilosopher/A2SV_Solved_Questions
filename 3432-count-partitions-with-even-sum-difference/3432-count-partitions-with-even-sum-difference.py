class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        _sum,count=0,0
        prefix=[_sum:=_sum+num for num in nums]
 

        for p in prefix:
            j=prefix[-1]-p
            if (p-j)%2==0:
                count+=1
        return count-1 if count else 0
        
        
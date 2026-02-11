class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        counted=Counter(nums)
        x,f=0,0
        for key,val in counted.items():
            if val>f:
                f=val
                x=key

        index=0
        left=0
        while index<len(nums)-1:
            if nums[index]==x:
                left+=1
  

            right=f-left
            if left*2>index+1 and right*2>len(nums)-index-1:
                return index
            index+=1
 
        return -1
        
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
   
        prefleft=[0]*len(nums)
        prefright=[0]*len(nums)
        left,right=nums[0],nums[-1]

        for i in range(1,len(nums)):
            prefleft[i]=left
            left+=nums[i]
        for j in range(len(nums)-2,-1,-1):
            prefright[j]=right
            right+=nums[j]

        ans=[0]*len(nums)
        for i in range(len(nums)):
            ans[i]=(abs(prefleft[i]-prefright[i]))

        return ans
            
        

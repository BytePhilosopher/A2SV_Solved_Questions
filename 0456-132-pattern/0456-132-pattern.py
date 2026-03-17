class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk=[]

        min_val=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<min_val:
                return True

            while stk and stk[-1]<nums[i]:
                min_val=stk.pop()

            stk.append(nums[i])

        return False
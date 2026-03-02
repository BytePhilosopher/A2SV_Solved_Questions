class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left = 0

        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left)

        return max_length
        # maxim=0
        # count=0
        # if 0 not in nums:
        #     return len(nums)-1

        # for i in range(len(nums)):
        #     temp=0
        #     j=i
        #     while j<len(nums) and nums[j]!=0:
        #         temp+=1
        #         j+=1
        #     if temp:
        #         counter1=0
        #         counter=0
        #         k=i+temp-1
        #         if k+2<len(nums):
        #             if nums[k+1]==0 and nums[k+2]==1:
        #                 r=k+2
        #                 while r<len(nums) and nums[r]==1:
        #                     r+=1
        #                     counter+=1
        #         if i-2>=0 and nums[i-1]==0 and nums[i-2]==1:
        #                 r=i-2
        #                 while r>=0 and nums[r]==1:
        #                     r-=1
        #                     counter1+=1
        #         counted=max(counter,counter1)
        #         count=max(count,counted+temp)

        # return count if temp else 0

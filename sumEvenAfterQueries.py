class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        x=sum([k for k in nums if k%2==0 ])
        for i in range(len(queries)):
            num=nums[queries[i][1]]
            added=queries[i][0]

            nums[queries[i][1]]+=added
            if nums[queries[i][1]] %2==0 and num%2!=0:
                x+=nums[queries[i][1]]
            elif nums[queries[i][1]] %2==0 and num%2==0:
                x-=num
                x+=nums[queries[i][1]]
            elif num%2==0:
                x-=num
            ans.append(x)



        return ans
        
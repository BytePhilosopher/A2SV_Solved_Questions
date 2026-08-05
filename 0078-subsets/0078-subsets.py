class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]

        def dfs(start):

            #base case
            
            result.append(path[:])
           

            
            # print(path)
            for index in range(start,len(nums)):
                path.append(nums[index])
                dfs(index+1)
                path.pop()

            

        dfs(0)
   
        return result


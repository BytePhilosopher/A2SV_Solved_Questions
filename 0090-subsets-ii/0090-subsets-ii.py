class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        nums.sort()
        seen=set()

        def dfs(start):

            #base case
            
            result.append(path[:])
           

            
            # print(path)
            for index in range(start,len(nums)):
                if index>0 and nums[index] not in seen and nums[index]==nums[index-1]:
                    continue
                path.append(nums[index])
                seen.add(nums[index])
                dfs(index+1)
                seen.discard(nums[index])
                path.pop()
                

            

        dfs(0)
   
        return result


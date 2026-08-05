class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)

        curset=[]

        def dfs(cur,ind):
            #base case
            
            result.append(cur[:])
   

            for i in range(ind,len(nums)):
                #choose
                cur.append(nums[i])
                dfs(cur, i+1)
                #unchoose
                cur.pop()

        dfs([],0)
        return result


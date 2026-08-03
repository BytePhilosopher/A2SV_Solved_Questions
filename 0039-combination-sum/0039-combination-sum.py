class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()

        def combsum(j,temp,cursum):
            if cursum==target:
                ans.append(temp[:])
                return
            if cursum>target:
                return
            
            
            
            #takr 
            for i in range(j,len(candidates)):
                if cursum + candidates[i]<=target :
                    temp.append(candidates[i])
                    combsum(i,temp,cursum + candidates[i])
                    temp.pop()
                # print(temp)
            
            

        combsum(0,[],0)


        return ans 
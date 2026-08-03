class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()

        def combsum(j,temp,cursum):
            if cursum==target:
                ans.append(temp[:])
                return
            if cursum>target or j>=len(candidates):
                return
            
            
            
            #takr 
            if cursum + candidates[j]<=target :
                temp.append(candidates[j])
                combsum(j,temp,cursum + candidates[j])
                temp.pop()
            combsum(j+1,temp, cursum)
    
            print(temp)
            
            

        combsum(0,[],0)


        return ans 
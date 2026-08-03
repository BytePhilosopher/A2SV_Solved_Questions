class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()

        def combsum(j,temp):
            if sum(temp)==target:
                ans.append(temp[:])
                return
            if sum(temp)>target or j == len(candidates):
                return
            
            
            
            #takr 
            temp.append(candidates[j])
            combsum(j,temp)
            temp.pop()


            #skip
            combsum(j+1,temp)
    
            print(temp)
            
            

        combsum(0,[])


        return ans 
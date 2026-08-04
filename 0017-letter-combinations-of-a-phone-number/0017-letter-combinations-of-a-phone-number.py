class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],
              "6":["m","n","o"], "7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}

        result=[]

        def dfs(i,j,temp):
            #base case
            if len(digits)==len(temp):
                result.append("".join(temp))
                return

            if i>=len(digits) or j>=len(hash[digits[i]]):
                return
            
            temp.append(hash[digits[i]][j])
            dfs(i+1,0,temp)
            temp.pop()

            dfs(i,j+1,temp)

            
        dfs(0,0,[])
        return result
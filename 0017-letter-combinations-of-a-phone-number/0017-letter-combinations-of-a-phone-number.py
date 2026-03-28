class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],
              "6":["m","n","o"], "7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        ans=[]
        def dfs(cur,i):
            if i==len(digits):
                ans.append("".join(cur))
                return


            for j in range(len(hash[digits[i]])):
                cur.append(hash[digits[i]][j])
                print(cur)
                dfs(cur,i+1)
                cur.pop()
        dfs([],0)
        return ans

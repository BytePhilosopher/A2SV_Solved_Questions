class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i,j,ind):
            #if we get
            if ind==len(word):
                return True
            if (i<0 or i>=len(board)) or (j<0 or j>=len(board[0])) or board[i][j]!=word[ind]:
                return False

            temp=board[i][j]
            board[i][j]="#"

            found=( dfs(i+1,j,ind+1) or 
               dfs(i,j-1,ind+1) or 
               dfs(i,j+1,ind+1) or 
               dfs(i-1,j,ind+1))
            

            #backtrack
            board[i][j]=temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
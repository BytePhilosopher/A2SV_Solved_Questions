class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        dx=[False]*(n*2)
        dy=[False]*(n *2)
        cols=[False]*n
        result=[]

        board=[["."]*n for _ in range(n)]

        def dfs(index):

            if index==n:
                result.append(["".join(rows) for rows in board])
                return

            for col in range(n):
                if cols[col] or dx[col+index] or dy[index-col+n]:
                    continue
                
                dx[col+index]=True
                dy[index-col+n]=True
                cols[col]=True
                board[index][col]="Q"

                dfs(index+1)
            
                dx[col+index]=False
                dy[index-col+n]=False
                cols[col]=False
                board[index][col]="."

        dfs(0)

        return result
                

            
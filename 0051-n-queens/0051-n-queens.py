class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        dx=set()
        dy=set()
        column=[False]*n
        board=[["."]*n for _ in range(n)]

        def backtrack(row):
            #base case

            if row==n:
                result.append(["".join(rows) for rows in board])
                return
            
            for col in range(n):
                if column[col] or (row-col) in dy or(row + col) in dx:
                    continue

                board[row][col]="Q"
                dx.add(row+col)
                dy.add(row-col)
                column[col]=True

                backtrack(row+1)

                board[row][col]="."
                dx.remove(row+col)
                dy.remove(row-col)
                column[col]=False

        backtrack(0)
        return result
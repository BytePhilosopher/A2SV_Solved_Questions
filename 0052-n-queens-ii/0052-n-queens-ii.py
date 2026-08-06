class Solution:
    def totalNQueens(self, n: int) -> int:
        result=[]
        dx=set()
        dy=set()
        column=[False]*n
        count=0
       
        def backtrack(row):
            #base case
            nonlocal count
            if row==n:
                count+=1
                return
            
            for col in range(n):
                if column[col] or (row-col) in dy or(row + col) in dx:
                    continue

          
                dx.add(row+col)
                dy.add(row-col)
                column[col]=True

                backtrack(row+1)


                dx.remove(row+col)
                dy.remove(row-col)
                column[col]=False

        backtrack(0)
        return count
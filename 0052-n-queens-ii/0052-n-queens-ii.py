class Solution:
    def totalNQueens(self, n: int) -> int:
        dx=set()
        dy=set()
        cols=set()
        ans=[["."]*n for _ in range(n)]
        count=0

        def dfs(i):
            nonlocal count
            if i==n:
                count+=1
                return

            for j in range(n):
                if i-j in dx or i+j in dy or j in cols:
                    continue
                ans[i][j]="Q"
                dx.add(i-j)
                dy.add(i+j)
                cols.add(j)
                dfs(i+1)
                ans[i][j]="."
                dx.remove(i-j)
                dy.remove(i+j)
                cols.remove(j)
        dfs(0)
        return count
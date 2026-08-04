class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        dx=set()
        dy=set()
        cols=set()
        res=[["."]*n for _ in range(n) ]
        print(res)
        ans=[]

        def dfs(i):
            #base case
            if i==n:
                ans.append(["".join(k) for k in res])
                return

            for j in range(n):
                if i-j not in dy and i+j not in dx and j not in cols:
                    dx.add(i+j)
                    dy.add(i-j)
                    cols.add(j)
                    res[i][j]="Q"

                    dfs(i+1)

                    #backtrack
                    res[i][j]="."
                    dx.remove(i+j)
                    dy.remove(i-j)
                    cols.remove(j)

        dfs(0)
        return ans

            
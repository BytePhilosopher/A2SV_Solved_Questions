class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        counter=0

        for r in range(n):
            for c in range(m):
                if grid[r][c]<0:
                    counter+=1

        return counter

        
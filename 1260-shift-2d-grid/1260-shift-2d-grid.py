class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row=len(grid)
        col=len(grid[0])
        for _ in range(k):
            ngrid = [[0]*col for _ in range(row)]

            for r in range(row):
                for c in range(col-1):
                    ngrid[r][c+1] = grid[r][c]

            for r in range(row-1):
                ngrid[r+1][0] = grid[r][col-1]

            ngrid[0][0] = grid[row-1][col-1]

            grid = ngrid
        return grid if k==0 else ngrid
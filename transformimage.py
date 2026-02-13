class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #(0,0) ->(0,2).   (0,1) -> (1,2).  (0,2)-> (2,2). col to last and row increas
        #(1,0) ->(0,1).    (1,1)-> (1,1)    (1,2)->(2,1)  reverse
        #(2,0) ->(0,0)     (2,1) ->(1,0)     (2,2)->(2,0) col to last
        n=len(matrix)
        newmat=[[0]*n for _ in range(n)]


        for row in range(n):
            newrow=0
            for col in range(n):
                newcol=n-row-1
                newmat[newrow][newcol]=matrix[row][col]
                newrow+=1
        for r in range(n):
            for c in range(n):
                matrix[r][c]=newmat[r][c]
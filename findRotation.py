class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        

        i=0
        while i<4:
            if mat==target:
                return True
            
            newmat=[[0]*n for _ in range(n)]
            for row in range(n):
                for col in range(n):
                    newcol=n-row-1
                    newmat[col][newcol]=mat[row][col]
            i+=1
            mat=newmat
        return False
        
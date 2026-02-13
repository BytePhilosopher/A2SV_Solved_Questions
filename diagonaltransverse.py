import itertools


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans={}
    
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                s = i + j
                if s not in ans:
                    ans[s] = []
                ans[s].append(mat[i][j])

        sum=len(mat)+len(mat[0])-1
        res=[]
        for r in range(sum):
            if r%2==0:
                ans[r]=ans[r][::-1]

        return list(itertools.chain.from_iterable(ans.values()))


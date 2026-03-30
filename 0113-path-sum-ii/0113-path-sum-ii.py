# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        tot=0
        def dfs(root,temp,cursum):
            cursum+=root.val
            path=temp+[root.val]
            
            if root.left:
                dfs(root.left,path,cursum)
            if root.right:
                dfs(root.right,path,cursum)
            if not root.left and not root.right and cursum==targetSum:
                ans.append(path)
        if not root: return []
        dfs(root,[],0)
        return ans
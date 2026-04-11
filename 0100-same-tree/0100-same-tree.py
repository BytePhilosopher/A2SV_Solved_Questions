# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        x=True
        def dfs(p,q):
            nonlocal x
            if (not p and q) or (not q and p):
                x=False
            if not p or not q:
                return
            print(p.val,q.val)
            if p.val!=q.val:
                x=False
            dfs(p.left,q.left)
            dfs(p.right,q.right)
        dfs(p,q)
       
        return x
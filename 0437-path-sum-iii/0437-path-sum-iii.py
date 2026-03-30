# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def count_paths(node, target):
            if not node:
                return 0
            
            res = 0
            if node.val == target:
                res += 1
            
            res += count_paths(node.left, target - node.val)
            res += count_paths(node.right, target - node.val)
            
            return res

        def dfs(node):
            if not node:
                return 0
            
            return (
                count_paths(node, targetSum) +
                dfs(node.left) +
                dfs(node.right)
            )

        return dfs(root)
        return count
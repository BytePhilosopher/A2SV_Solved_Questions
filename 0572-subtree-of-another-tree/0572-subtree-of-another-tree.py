class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return isSame(a.left, b.left) and isSame(a.right, b.right)

        def dfs(root):
            if not root:
                return False
            if isSame(root, subRoot):
                return True
            return dfs(root.left) or dfs(root.right)

        return dfs(root)
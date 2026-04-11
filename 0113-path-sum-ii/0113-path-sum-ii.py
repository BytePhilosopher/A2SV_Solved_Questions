# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        temp=[]
        def dfs(root,target):
            if not root:
                return
            cursum=target-root.val
            temp.append(root.val)
            if not root.left and not root.right and root.val==target:
                ans.append(temp[:])
            
            dfs(root.left,cursum)
            dfs(root.right,cursum)
            temp.pop()

        if not root: return []
        dfs(root,targetSum)
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSumBST(self, root):
        self.ans = 0

        def dfs(node):
            # returns:
            # (isBST, minVal, maxVal, sum)

            if not node:
                return (True, float('inf'), -float('inf'), 0)

            leftBST, leftMin, leftMax, leftSum = dfs(node.left)
            rightBST, rightMin, rightMax, rightSum = dfs(node.right)

            # check BST property
            if leftBST and rightBST and leftMax < node.val < rightMin:

                currSum = leftSum + rightSum + node.val

                self.ans = max(self.ans, currSum)

                return (
                    True,
                    min(leftMin, node.val),
                    max(rightMax, node.val),
                    currSum
                )

            # not BST
            return (False, 0, 0, 0)

        dfs(root)
        return self.ans
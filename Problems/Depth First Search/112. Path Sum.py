# https://leetcode.com/problems/path-sum/submissions/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, s=0):
            if not node:
                return False
            s += node.val
            if not node.left and not node.right:
                return s == targetSum
            return dfs(node.left, s) or dfs(node.right, s)

        return dfs(root)

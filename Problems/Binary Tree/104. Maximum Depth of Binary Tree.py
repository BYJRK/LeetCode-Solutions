# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def getMaxDepth(node: TreeNode) -> int:
            if node is None:
                return 0
            return max(getMaxDepth(node.left), getMaxDepth(node.right)) + 1

        return getMaxDepth(root)

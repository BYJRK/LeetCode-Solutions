# https://leetcode.com/problems/minimum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def getMinDepth(node: TreeNode) -> int:
            if node is None:
                return 0
            if node.left is None:
                return getMinDepth(node.right) + 1
            elif node.right is None:
                return getMinDepth(node.left) + 1
            else:
                return min(getMinDepth(node.left), getMinDepth(node.right)) + 1

        return getMinDepth(root)


s = Solution()

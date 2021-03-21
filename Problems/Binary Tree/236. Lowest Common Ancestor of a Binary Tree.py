# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = None

        def findLCA(node):
            if node is None:
                return 0
            count = 0
            if node == p or node == q:
                count += 1
            count += findLCA(node.left)
            count += findLCA(node.right)
            if count == 2:
                nonlocal res
                if res is not None:
                    return
                res = node
            return count

        findLCA(root)

        return res

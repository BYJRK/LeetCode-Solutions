# https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isValid(node, min_=None, max_=None) -> bool:
            """
            判断某个节点是否为 BST
            要观察
            """
            if node is None:
                return True
            if max_ and node.val >= max_.val:
                return False
            if min_ and node.val <= min_.val:
                return False
            return isValid(node.left, min_, node) and isValid(node.right, node, max_)

        return isValid(root)

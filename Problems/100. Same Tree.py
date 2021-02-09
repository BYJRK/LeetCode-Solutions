# https://leetcode.com/problems/same-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


s = Solution()
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(s.isSameTree(tree1, tree1))

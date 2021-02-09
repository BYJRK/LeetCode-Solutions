# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None:
            self.flatten(root.right)
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left

        # 将当前的 right 添加到 left 的末端
        p = left
        while p.right is not None:
            p = p.right
        p.right = root.right
        # 交换 left 和 right，并将 left 置为 None
        root.right = left
        root.left = None

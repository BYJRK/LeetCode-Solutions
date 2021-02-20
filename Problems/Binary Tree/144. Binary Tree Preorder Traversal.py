# https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal_recur(self, root: TreeNode) -> List[int]:

        res = []

        def dfs(node):
            if node == None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def preorderTraversal_iter(self, root: TreeNode) -> List[int]:

        res = []
        stack = []
        node = root

        while len(stack) > 0 or node is not None:
            while node is not None:
                stack.append(node)
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right

        return res

# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_dfs(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def inorderTraversal_iter(self, root: TreeNode) -> List[int]:

        res = []
        stack = []
        node = root
        while len(stack) > 0 or node != None:
            # 只要有 left 节点，就全部加进去，加到找不到 left 节点为止
            while node != None:
                stack.append(node)
                node = node.left
            # 最后加入的 node.left 已经是 None，所以删除掉
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

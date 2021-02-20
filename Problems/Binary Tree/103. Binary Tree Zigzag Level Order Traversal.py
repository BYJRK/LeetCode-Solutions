# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []

        def dfs(node, level=0):
            if node == None:
                return
            if len(res) == level:
                res.append([node.val])
            else:
                if level % 2 == 1:
                    res[level].insert(0, node.val)
                else:
                    res[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root)
        return res

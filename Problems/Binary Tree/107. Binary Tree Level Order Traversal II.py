# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = deque()

        def dfs(node, level=0):
            if node == None:
                return
            while len(res) <= level:
                res.appendleft([])
            res[-(level+1)].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root)
        return res

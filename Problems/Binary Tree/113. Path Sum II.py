# https://leetcode.com/problems/path-sum-ii/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        res = []

        def dfs(node, cur=[], s=0):
            if node is None:
                return
            if node.left is None and node.right is None:
                if s + node.val == targetSum:
                    res.append(cur + [node.val])
            dfs(node.left, cur + [node.val], s + node.val)
            dfs(node.right, cur + [node.val], s + node.val)

        dfs(root)

        return res

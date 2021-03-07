# https://leetcode.com/problems/path-sum-iii/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        res = 0

        def dfs(node, path=[]):
            if not node:
                return
            path.append(node)
            s = 0
            for n in reversed(path):
                s += n.val
                if s == sum:
                    nonlocal res
                    res += 1
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root)

        return res

# https://leetcode.com/problems/binary-tree-paths/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        paths = []

        def dfs(node, path=[]):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                paths.append(path.copy())
                path.pop()
                return
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root)

        ans = []
        for r in paths:
            ans.append('->'.join([str(v) for v in r]))

        return ans

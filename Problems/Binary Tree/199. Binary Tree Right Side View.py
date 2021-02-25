# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView_dfs(self, root: TreeNode) -> List[int]:
        layers = []

        def dfs(node, level=0):
            if node is None:
                return
            while level >= len(layers):
                layers.append([])
            layers[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root)

        return [layer[-1] for layer in layers]

    def rightSideView_bfs(self, root: TreeNode) -> List[int]:
        res = []
        queue = [root]
        curSum = 1
        nextSum = 0
        curLayer = []
        while len(queue) > 0:
            if curSum > 0:
                node = queue[0]
                if node.left is not None:
                    queue.append(node.left)
                    nextSum += 1
                if node.right is not None:
                    queue.append(node.right)
                    nextSum += 1
                curLayer.append(node.val)
                queue.pop(0)
                curSum -= 1
            else:
                res.append(curLayer)
                curLayer = []
                curSum = nextSum
                nextSum = 0
        return [layer[-1] for layer in res]

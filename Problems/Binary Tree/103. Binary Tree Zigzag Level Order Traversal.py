# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List


from collections import deque

queue = deque()
queue.append(0)
pop = queue.popleft()


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder_dfs(self, root: TreeNode) -> List[List[int]]:

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

    def zigzagLevelOrder_bfs(self, root: TreeNode) -> List[List[int]]:

        res = []

        queue = [root]
        curSum = 1
        nextSum = 0
        curLayer = []

        isReversed = True

        while len(queue) > 0:
            if curSum > 0:
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                    nextSum += 1
                if node.right is not None:
                    queue.append(node.right)
                    nextSum += 1
                curLayer.append(node.val)
                curSum -= 1
            if curSum == 0:
                isReversed = not isReversed
                if isReversed:
                    curLayer.reverse()
                res.append(curLayer)
                curLayer.clear()
                curSum = nextSum
                nextSum = 0

        return res

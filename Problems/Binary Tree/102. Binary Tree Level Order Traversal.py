# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder_bfs(self, root: TreeNode) -> List[List[int]]:

        res = []

        queue = [root]
        nextNum = 0  # 下一层有多少个节点
        curNum = 1  # 当前层h还有多少个节点需要遍历
        tmp = []

        while len(queue) > 0:
            # 如果当前层还有节点要遍历
            if curNum > 0:
                node = queue[0]
                if node.left != None:
                    queue.append(node.left)
                    nextNum += 1
                if node.right != None:
                    queue.append(node.right)
                    nextNum += 1
                curNum -= 1
                tmp.append(node.val)
                queue.pop(0)
            # 如果已经没有要遍历的节点了，移动到下一层
            if curNum == 0:
                res.append(tmp)
                curNum = nextNum
                nextNum = 0
                tmp = []

        return res

    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:

        res = []

        def dfs(node: TreeNode, level: int) -> None:
            if node == None:
                return
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            if node.left != None:
                dfs(node.left, level + 1)
            if node.right != None:
                dfs(node.right, level + 1)

        dfs(root, 0)
        return res

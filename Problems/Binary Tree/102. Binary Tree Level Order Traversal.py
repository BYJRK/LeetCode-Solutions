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
        curNum = 1  # 当前层还有多少个节点需要遍历
        nextNum = 0  # 下一层有多少个节点
        curLayer = []

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
                curLayer.append(node.val)
                queue.pop(0)

            # 如果已经没有要遍历的节点了，移动到下一层
            # 注意这里不能写 else，因为有可能正好在上面将 queue 中最后一个 pop 掉了
            # 此时 tmp 里面还有内容没有追加
            if curNum == 0:
                res.append(curLayer)
                curNum = nextNum
                nextNum = 0
                curLayer = []

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

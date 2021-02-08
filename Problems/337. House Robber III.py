# https://leetcode.com/problems/house-robber-iii/

from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            """
            返回值为当前节点没有/有被打劫的最大值
            """
            if not node:
                return 0, 0
            l0, l1 = dfs(node.left)
            r0, r1 = dfs(node.right)

            # 如果不抢当前节点，则抢两个子节点（但是也有可能继续不抢子节点）
            c0 = max(l0, l1) + max(r0, r1)
            # 如果抢当前节点，则不抢两个子节点（但是抢子节点的子节点）
            c1 = l0 + r0 + node.val

            return c0, c1

        return max(dfs(root))


s = Solution()
tree1 = TreeNode(3,
                 TreeNode(2, right=TreeNode(3)),
                 TreeNode(3, right=TreeNode(1))
                 )  # 7
tree2 = TreeNode(3,
                 TreeNode(4, TreeNode(1), TreeNode(3)),
                 TreeNode(5, right=TreeNode(1))
                 )  # 9
print(s.rob(tree1))
print(s.rob(tree2))

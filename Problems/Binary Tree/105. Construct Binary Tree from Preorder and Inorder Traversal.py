# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(preorder: List[int], inorder: List[int]) -> TreeNode:

            if not preorder or not inorder:
                return None

            # 这个 idx 不仅表示当前的 pre[0]，也就是 root 在 in 中的位置
            # 同时还表示 root 左边有几个
            root_idx = inorder.index(preorder[0])
            tree = TreeNode(preorder[0])

            # 对于 inorder 来说，找到 root 后，其左侧都是 left 节点的，右侧同理
            inorder_left = inorder[:root_idx]
            inorder_right = inorder[root_idx + 1:]

            # 假如 idx = 3，那也就是说在当前的 inorder 中，root 在第 4 个的位置
            # root 前面的三个都是属于其 left 节点的
            # 所以回到 preorder，root 后面的三个都是属于其 left 节点的
            # 剩下的是 right 节点的
            preorder_left = preorder[1:root_idx + 1]
            preorder_right = preorder[root_idx + 1:]

            tree.left = dfs(preorder_left, inorder_left)
            tree.right = dfs(preorder_right, inorder_right)

            return tree

        return dfs(preorder, inorder)

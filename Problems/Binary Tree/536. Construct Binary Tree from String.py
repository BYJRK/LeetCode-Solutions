# https://leetcode.com/problems/construct-binary-tree-from-string/


from typing import List
import re


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        tokens = re.findall(r'\d+|\(|\)', s)
        idx = 0

        def func() -> TreeNode:
            # 每一层对应的情况形如：
            # 10
            # 10(2)
            # 10()(5)
            # 10(2)(5)
            nonlocal idx
            if idx >= len(tokens):
                return None
            node = None
            if tokens[idx].isdigit():
                node = TreeNode(int(tokens[idx]))
                # 数字后面除了结尾，只可能是左右括号
                idx += 1
                if idx < len(tokens) and tokens[idx] == '(':
                    # 在开头和结尾跳过括号
                    idx += 1
                    node.left = func()
                    idx += 1
                if idx < len(tokens) and tokens[idx] == '(':
                    idx += 1
                    node.right = func()
                    idx += 1
            return node

        res = func()
        return res

    def str2tree_stack(self, s: str) -> TreeNode:
        tokens = re.findall(r'\d+|\(|\)', s)
        idx = 0

        def pair(idx):
            left = right = idx
            stack = [tokens[left]]
            while stack:
                right += 1
                token = tokens[right]
                if token == ')':
                    while (p := stack.pop()) != '(':
                        pass
                else:
                    stack.append(token)
            return left, right

        def func(l, r) -> TreeNode:
            # 每一层对应的情况形如：空，10，10(2)，10()(5)，10(2)(5)
            idx = l
            if not tokens[idx].isdigit():
                return None
            node = TreeNode(int(tokens[idx]))
            if idx + 1 < len(tokens) and tokens[idx + 1] == '(':
                l, r = pair(idx + 1)
                node.left = func(l + 1, r - 1)
                idx = r
            if idx + 1 < len(tokens) and tokens[idx + 1] == '(':
                l, r = pair(idx + 1)
                node.right = func(l + 1, r - 1)
                idx = r
            return node

        res = func(0, len(tokens) - 1)
        return res

    def preorder(self, node: TreeNode) -> None:
        res = []

        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(node)

        return res


s = Solution()
# tree = s.str2tree('1(2()(4))(3)')
# tree = s.str2tree('1(2(4))(3)')
tree = s.str2tree_stack('1(2(4()(5)))(3(6)(7(8)))')
print(s.preorder(tree))

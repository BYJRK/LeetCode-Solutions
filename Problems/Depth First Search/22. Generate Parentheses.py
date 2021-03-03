# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def dfs(cur, left: int, right: int):
            '''
            left right 分别表示左右括号还剩多少个可以用
            这个在理解 right > left 上稍微有一点困难
            实际上是 n - left > n - right，也就是已经写上的左括号数量一定要大于右括号的
            化简得到 right > left
            '''
            if left == 0 and right == 0:
                res.append(cur)
            if left > 0:
                dfs(cur + '(', left - 1, right)
            if right > 0 and right > left:
                dfs(cur + ')', left, right - 1)

        def dfs2(cur, left: int, right: int):
            '''
            跟上面的基本一样，但是相对更好理解
            '''
            if left == n and right == n:
                res.append(cur)
            if left < n:
                dfs2(cur + '(', left + 1, right)
            if right < n and right < left:
                dfs2(cur + ')', left, right + 1)

        # dfs('', n, n)
        dfs2('', 0, 0)

        return res


s = Solution()
print(s.generateParenthesis(3))

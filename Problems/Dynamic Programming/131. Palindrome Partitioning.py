# https://leetcode.com/problems/palindrome-partitioning/submissions/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # dp[i] 表示 s[:i] 的所有拆分方式，i 从 1 开始
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [[]]

        def isPalindrome(t):
            '''判断 t 是否为回文'''
            if len(t) == 1:
                return True

            i, j = 0, len(t) - 1
            while i < j:
                if t[i] != t[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(0, len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                tmp = s[i:j]
                if isPalindrome(tmp):
                    for comb in dp[i]:
                        dp[j].append(comb + [tmp])

        return dp[-1]

    def partition_v2(self, s: str) -> List[List[str]]:

        def isPalindrome(t: str):
            '''判断 t 是否为回文'''
            if len(t) == 1:
                return True
            mid = len(t) // 2
            return t[:mid] == t[-mid:][::-1]

        def dfs(s: str, memo={}):
            if s in memo:
                return memo[s]
            # 在搜索的最后，发现拆分得只剩下一个字母，那说明这条路行得通
            if len(s) == 1:
                return [[s]]

            res = []
            for i in range(1, len(s)):
                left, right = s[:i], s[i:]
                if isPalindrome(left):
                    ways = dfs(right, memo)
                    for way in ways:
                        res.append([left] + way)

            # 如果经历了上面的循环之后，并没有找到结果，那么此时 res = []
            memo[s] = res
            return res

        return dfs(s)


s = Solution()
print(s.partition_v2('aaab'))

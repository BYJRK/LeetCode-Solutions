# https://leetcode.com/problems/integer-break/

from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, i):
                # 有三种可能：
                # 1. 当前数字（指的是先前用别的方式算出来的）
                # 2. 5 -> 3 x 2
                # 3. 5 -> 3 x (1 x 1)
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))

        return dp[-1]

    def integerBreakII(self, n: int):
        dp = [[0, []] for _ in range(n + 1)]

        for i in range(2, n+1):
            for j in range(1, i):
                cur = dp[i][0]
                s1 = j * dp[i-j][0]
                s2 = j * (i - j)
                if cur > max(s1, s2):
                    continue
                elif s1 > s2:
                    dp[i] = [s1, dp[i-j][1] + [j]]
                else:
                    dp[i] = [s2, [j, i-j]]

        return dp[-1]


s = Solution()
print(s.integerBreakII(20))  # 3x3x4

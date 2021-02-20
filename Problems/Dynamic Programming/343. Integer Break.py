# https://leetcode.com/problems/integer-break/submissions/

class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n + 1):
            for j in range(1, i):
                # 有三种可能：
                # 1. 当前数字（指的是先前用别的方式算出来的）
                # 2. 5 -> 3 x 2
                # 3. 5 -> 3 x (1 x 1)
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))

        return dp[-1]

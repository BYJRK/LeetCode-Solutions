# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    dp[i+1][j] += dp[i][j]
                if j + 1 < n:
                    dp[i][j+1] += dp[i][j]

        return dp[-1][-1]

    def uniquePaths_v2(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[-1]


s = Solution()
print(s.uniquePaths_v2(3, 7))
print(s.uniquePaths_v2(5, 5))

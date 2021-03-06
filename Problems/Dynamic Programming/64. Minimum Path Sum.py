# https://leetcode.com/problems/minimum-path-sum/

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    val = dp[i][j] + grid[i+1][j]
                    dp[i+1][j] = val if dp[i +
                                           1][j] == 0 else min(dp[i+1][j], val)
                if j + 1 < n:
                    val = dp[i][j] + grid[i][j+1]
                    dp[i][j+1] = val if dp[i][j +
                                              1] == 0 else min(dp[i][j+1], val)

        return dp[-1][-1]

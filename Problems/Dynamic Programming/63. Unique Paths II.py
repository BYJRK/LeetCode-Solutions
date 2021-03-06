# https://leetcode.com/problems/unique-paths-ii/

from typing import List
from collections import deque


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                # right
                if j + 1 < n and obstacleGrid[i][j+1] != 1:
                    dp[i][j+1] += dp[i][j]
                # down
                if i + 1 < m and obstacleGrid[i+1][j] != 1:
                    dp[i+1][j] += dp[i][j]

        return dp[-1][-1]


s = Solution()
grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid2 = [[0, 0], [0, 1]]
print(s.uniquePathsWithObstacles(grid1))
print(s.uniquePathsWithObstacles(grid2))

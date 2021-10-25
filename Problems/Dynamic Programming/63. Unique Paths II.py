# https://leetcode.com/problems/unique-paths-ii/

from typing import List
from collections import deque


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                # right
                if j + 1 < n and obstacleGrid[i][j + 1] != 1:
                    dp[i][j + 1] += dp[i][j]
                # down
                if i + 1 < m and obstacleGrid[i + 1][j] != 1:
                    dp[i + 1][j] += dp[i][j]

        return dp[-1][-1]

    def uniquePathsWithObstacles_v2(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1

        for i in range(m):
            # 因为最左边一列也有可能有障碍物，所以不能从每行第二个开始更新
            for j in range(n):
                # 如果当前位置是障碍物
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j - 1 >= 0:
                    dp[j] += dp[j - 1]
        return dp[-1]


s = Solution()
grid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
grid2 = [[0, 0], [1, 0]]
grid3 = [[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]]
print(s.uniquePathsWithObstacles(grid1))
print(s.uniquePathsWithObstacles_v2(grid2))
print(s.uniquePathsWithObstacles(grid3))
print(s.uniquePathsWithObstacles_v2(grid3))

# https://leetcode.com/problems/triangle/

from typing import List


class Solution:
    def minimumTotal_v1(self, triangle: List[List[int]]) -> int:
        layers = len(triangle)
        if layers == 1:
            return triangle[0][0]
        dp = [[0 for _ in range(layers)] for _ in range(layers)]
        dp[0][0] = triangle[0][0]

        for i in range(1, layers):
            for j in range(len(triangle[i])):
                cur = triangle[i][j]
                # head
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + cur
                # tail
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + cur
                # middle
                else:
                    dp[i][j] = min(dp[i - 1][j - 1:j + 1]) + cur

        return min(dp[-1])

    def minimumTotal_v2(self, triangle: List[List[int]]) -> int:
        layers = len(triangle)
        if layers == 1:
            return triangle[0][0]
        dp = [[None for _ in range(layers)] for _ in range(layers)]
        dp[0][0] = triangle[0][0]

        for i in range(0, layers - 1):
            for j in range(len(triangle[i])):
                cur = dp[i][j]
                left = cur + triangle[i + 1][j]
                right = cur + triangle[i + 1][j + 1]
                if dp[i + 1][j] is None or left < dp[i + 1][j]:
                    dp[i + 1][j] = left
                if dp[i + 1][j + 1] is None or right < dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = right

        return min(dp[-1])


s = Solution()
print(s.minimumTotal_v1([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
print(s.minimumTotal_v2([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11

# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost:     10  15  20
        # dp:    0   0   0   0   0
        # index: 0   1   2   3   4
        # 比 cost 多一个开头和结尾，表示起点和终点
        dp = [-1] * (len(cost) + 2)
        dp[0] = 0
        # 表示到达最顶端不需要额外花费力气
        cost += [0]
        for i in range(len(dp) - 1):
            if dp[i + 1] == -1:
                dp[i + 1] = dp[i] + cost[i]
            else:
                dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            if i + 2 >= len(dp):
                break
            if dp[i + 2] == -1:
                dp[i + 2] = dp[i] + cost[i + 1]
            else:
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i + 1])

        return dp[-1]


s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))  # 15
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6

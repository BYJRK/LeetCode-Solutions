# https://leetcode.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 表示凑够 n 有多少种方式
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount):
            if dp[i] == -1:
                continue
            cur = dp[i]+1
            for c in coins:
                if i + c > amount:
                    continue
                if dp[i + c] == -1:
                    dp[i + c] = cur
                elif dp[i + c] > cur:
                    dp[i + c] = cur
        return dp[-1]

    def coinChange_v1(self, coins: List[int], amount: int) -> int:

        min_coin = min(coins)

        def dfs(amount, memo={}) -> int:
            """
            计算对应 amount 所需的最少钱币数量（可能为 -1)
            """
            if amount in memo:
                return memo[amount]

            if amount == 0:
                return 0

            if amount < min_coin:
                return - 1

            res = [dfs(amount - c, memo) for c in coins]
            res = [r for r in res if r != -1]
            if len(res) == 0:
                memo[amount] = -1
                return -1
            else:
                memo[amount] = min(res) + 1
                return memo[amount]

        return dfs(amount)


s = Solution()
print(s.coinChange_v1([1, 2, 5], 11))  # 3
print(s.coinChange_v1([12, 9], 20))  # -1
print(s.coinChange_v1([186, 419, 83, 408], 6249))  # 20

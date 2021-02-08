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


s = Solution()
print(s.coinChange([1, 2, 5], 11))  # 3
print(s.coinChange([186, 419, 83, 408], 6249))  # 20

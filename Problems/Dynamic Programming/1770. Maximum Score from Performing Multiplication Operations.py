from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        l = len(multipliers)

        def dfs(i, j, idx=0, memo={}):
            key = f'{i},{j},{idx}'
            if key in memo:
                return memo[key]
            if idx >= len(multipliers):
                return 0
            res = max(nums[i] * multipliers[idx] + dfs(i + 1, j, idx + 1, memo),
                      nums[j] * multipliers[idx] + dfs(i, j - 1, idx + 1, memo))
            memo[key] = res
            return res

        return dfs(0, len(nums) - 1)

    def maximumScore_dp(self, nums: List[int], muls: List[int]) -> int:
        l = len(nums)
        dp = [[0 for _ in range(l)] for _ in range(l)]

        def getScore(i, j, idx=0):
            if idx >= len(muls):
                return 0
            if dp[i][j] == 0:
                dp[i][j] = max(nums[i] * muls[idx] + getScore(i + 1, j, idx + 1),
                               nums[j] * muls[idx] + getScore(i, j - 1, idx + 1))

            return dp[i][j]

        getScore(0, l - 1)
        return dp[0][-1]


nums = [-5, -3, -3, -2, 7, 1]
multipliers = [-10, -5, 3, 4, 6]

s = Solution()
print(s.maximumScore(nums, multipliers))
print(s.maximumScore_dp(nums, multipliers))

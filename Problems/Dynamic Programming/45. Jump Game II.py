# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def jump_v1(self, nums: List[int]) -> int:
        """
        从后往前，每次计算当前格子到结尾的最少步数
        """
        dp = [len(nums)] * len(nums)
        dp[-1] = 0
        for i in range(len(dp)-2, -1, -1):
            steps = dp[i+1:i+nums[i]+1]
            if not steps:
                continue
            dp[i] = min(steps) + 1
        return dp[0]

    def jump_v2(self, nums: List[int]) -> int:
        """
        从前往后，每次计算当前格子到前面所能到达的格子的最少步数
        如果找到了更少的，则更新
        """
        dp = [len(nums)] * len(nums)
        dp[0] = 0

        for i in range(len(dp)-1):
            for j in range(i+1, min(i+nums[i]+1, len(dp))):

                dp[j] = min(dp[j], dp[i] + 1)

        return dp[-1]


s = Solution()
print(s.jump_v1([2, 3, 1, 1, 4]))
print(s.jump_v1([2, 3, 0, 1, 4]))
print(s.jump_v2([2, 3, 1, 1, 4]))
print(s.jump_v2([2, 3, 0, 1, 4]))

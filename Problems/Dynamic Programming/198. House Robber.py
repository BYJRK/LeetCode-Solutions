# https://leetcode.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]

        # dp[i] 表示抢劫到第 i 间屋子时最多能抢多少
        dp = [-1] * l
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, l):
            # 10 5 1 6 1 3
            # 隔开上一个，从之前的两间屋子里挑选能抢最多的那间，然后加上这一间的
            dp[i] = max(dp[max(i - 3, 0):i - 1]) + nums[i]
        # 最后两间一定有一间会被抢，所以只需要从最后两个当中选出一个最大的即可
        return max(dp[-2:])

    def rob_v2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]


s = Solution()
print(s.rob([1, 2, 3, 1]))  # 4
print(s.rob([2, 7, 9, 3, 1]))  # 12

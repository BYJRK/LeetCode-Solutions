# https://leetcode.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        房子首尾相连，所以第一个和最后一个不能同时抢劫
        所以可以理解为分两次考虑
        一次不抢最后一个，一次不抢第一个
        然后比较哪次抢的比较多即可
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)

        r1 = self.robHouses(nums[:-1])
        r2 = self.robHouses(nums[1:])
        return max(r1, r2)

    def robHouses(self, nums: List[int]) -> int:
        """
        这个和 198. House Robber 完全一样
        """
        l = len(nums)
        dp = [-1] * l
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, l):
            dp[i] = max(dp[max(i - 3, 0):i - 1]) + nums[i]

        return max(dp[-2:])


s = Solution()
print(s.rob([2, 3, 2]))  # 3
print(s.rob([1, 2, 3, 1]))  # 4

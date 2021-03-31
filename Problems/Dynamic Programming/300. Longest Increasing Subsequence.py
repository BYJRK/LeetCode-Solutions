# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        for i, _ in enumerate(nums):
            if i == 0:
                dp[i] = 1
                continue
            # find max length with non-greater value
            max_ = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] > max_:
                        max_ = dp[j]
            dp[i] = max_ + 1
        return max(dp)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4

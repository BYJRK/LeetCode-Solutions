# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        maxDis = 0
        idx = 0
        while idx <= maxDis and idx < len(nums):
            maxDis = max(maxDis, idx + nums[idx])
            idx += 1
        return maxDis >= len(nums) - 1


s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([3, 2, 1, 0, 4]))
print(s.canJump([2, 0, 0]))

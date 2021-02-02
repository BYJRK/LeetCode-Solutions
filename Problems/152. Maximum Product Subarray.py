# https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)
        dp_max[0] = dp_min[0] = nums[0]

        for i in range(1, len(nums)):
            # 有三种情况：
            # 1. 前面的积或当前的数有负数
            # 2. 前面的积或当前的数有 0~1 的小数
            # 3. 乘完之后变大了（包含都是负数的可能）
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i],
                            dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], nums[i],
                            dp_min[i - 1] * nums[i])

        return max(dp_max)


s = Solution()
print(s.maxProduct([2, 3, -2, 4]))  # 6
print(s.maxProduct([-2, 0, -1]))  # 0
print(s.maxProduct([-2, 3, 1, -5, -1]))  # 30

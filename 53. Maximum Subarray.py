# https://leetcode.com/problems/maximum-subarray/

# 使用到的算法：https://en.wikipedia.org/wiki/Maximum_subarray_problem

from typing import List

# 基本思路：
#  1. 如果加了下一个数之后仍然是正数，那就还可以接受，先把前面的留着
#  2. 如果加了下一个（负）数之后和为 0 了，那可要可不要（看题目是否要求找最长的）
#  3. 如果当前的子数列的和已经是负数了，那直接舍掉，从下一个数开始重新寻找子数列
#     因为此时保留前面的子数列已经没有意义了，只能“帮倒忙”

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # _max：总体的子数列的最大值
        # cur：截止到目前位置的子数列的最大值
        _max = cur = nums[0]
        for n in nums[1:]:
            # 如果 cur 加上下一个值之后更大了，那说明下一个值是正数
            # 可以将其包含在最大子数列中
            if cur + n > n:
                cur += n
            # 如果反而变小了，那此时只有一种可能，即：
            #   前面的子数列和小于零。此时直接舍去前面的，从这个位置重新开始寻找子数列更为合适
            #   判断可以直接化简为：if cur > 0
            else:
                cur = n

            # 每次求得的最大子数列的和都保留一下
            # 因为有可能在前面已经找到了一个最大的，而后面的都没前面的这个大
            if cur > _max:
                _max = cur
        return _max


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # [4, -1, 2, 1] -> 6

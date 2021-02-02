# https://leetcode.com/problems/maximum-product-of-three-numbers/

from functools import reduce
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        def mul(a, b): return a * b
        nums.sort()
        # 有可能是三个最大的数字，也有可能是两个大负数和一个正数
        return max(reduce(mul, nums[-3:]), reduce(mul, nums[:2] + [nums[-1]]))


s = Solution()
print(s.maximumProduct([1, 2, 3, 4]))
print(s.maximumProduct([-1, -2, -3]))
print(s.maximumProduct([-1, -2, -3, 4]))

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def find_border(left_side: bool) -> int:
            res = -1
            p1, p2 = 0, len(nums) - 1
            while p1 <= p2:
                m = (p1 + p2 + 1) // 2
                if nums[m] < target:
                    p1 = m + 1
                elif nums[m] > target:
                    p2 = m - 1
                else:
                    res = m
                    if left_side:
                        p2 = m - 1
                    else:
                        p1 = m + 1
            return res

        left = find_border(True)
        if left == -1:
            return [-1, -1]
        right = find_border(False)
        return [left, right]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 9], 8))
print(s.searchRange([], 6))

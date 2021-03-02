# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            w = j - i
            h = min(height[i], height[j])
            area = w * h
            if area > res:
                res = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res

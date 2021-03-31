# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def calc(h: int) -> float:
            res = 0
            res += (h + max(0, h-index))*min(h+1, index+1)/2
            res += (h + max(0, h+index-n+1))*min(h+1, n-index)/2
            return res - h

        left = 0
        right = maxSum
        while left < right - 1:
            mid = (left + right) // 2
            if calc(mid) < maxSum:
                left = mid
            else:
                right = mid
        return left


s = Solution()
print(s.maxValue(5, 3, 10))

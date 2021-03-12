# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List


class Solution:
    def findMedianSortedArrays_v1(self, nums1: List[int],
                                  nums2: List[int]) -> float:
        """二分查找，复杂度 O(log(m+n))"""
        l1, l2 = 0, 0
        r1, r2 = len(nums1) - 1, len(nums2) - 1

        def findMedian(l1, r1, l2, r2):
            m1 = (r1 + l1) // 2
            m2 = (r2 + l2) // 2

        # unfinished

    def findMedianSortedArrays_v2(self, nums1: List[int],
                                  nums2: List[int]) -> float:
        """合并两个有序数组，复杂度 O(m+n)"""
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        l = l1 + l2
        mid = l // 2
        isEven = l % 2 == 0

        n1, n2 = 0, 0

        res = []

        while True:
            if i < l1 and j < l2:
                if nums1[i] < nums2[j]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            elif i >= l1 and j < l2:
                res.append(nums2[j])
                j += 1
            elif i < l1 and j >= l2:
                res.append(nums1[i])
                i += 1
            else:
                break

            if i + j == mid + 1:
                if isEven:
                    return sum(res[-2:]) / 2
                else:
                    return res[-1]


s = Solution()
print(s.findMedianSortedArrays_v1([1, 3, 5], [2, 4, 6]))

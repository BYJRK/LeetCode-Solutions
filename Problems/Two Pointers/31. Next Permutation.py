# https://leetcode.com/problems/next-permutation/

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 从右向左找到以一个比右边小的数字
        flag = False
        for idx in range(len(nums) - 2, -1, -1):
            if nums[idx + 1] > nums[idx]:
                flag = True
                break

        # 如果找到了，就将其与右边最小的比它大的数字进行交换
        if flag:
            minIdx = 0
            minVal = float('inf')
            for i in range(idx + 1, len(nums)):
                if nums[idx] < nums[i] <= minVal:
                    minVal = nums[i]
                    minIdx = i
            nums[idx], nums[minIdx] = nums[minIdx], nums[idx]

        # 将右边进行左右翻转
        l = idx + 1 if flag else 0
        r = len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


s = Solution()
# n1 = [1, 3, 4, 2]
# s.nextPermutation(n1)
# print(n1)
n2 = [2, 3, 1, 3, 3]
s.nextPermutation(n2)
print(n2)

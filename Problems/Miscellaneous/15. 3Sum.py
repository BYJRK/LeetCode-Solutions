# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        res = []
        dic = {n: i for i, n in enumerate(nums)}

        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j, b in enumerate(nums[i+1:]):
                if j > 0 and nums[i+j+1] == nums[i+j]:
                    continue
                c = 0 - a - b
                if c in dic and dic[c] >= i + j + 2:
                    res.append([a, b, c])

        return res

    def threeSum_v1(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        res = set()
        dic = {n: i for i, n in enumerate(nums)}

        for i in range(len(nums) - 2):
            a = nums[i]
            for j in range(i + 1, len(nums) - 1):
                b = nums[j]
                c = 0 - a - b
                if c in dic and dic[c] > j:
                    res.add((a, b, c))

        return list(res)


s = Solution()
print(s.threeSum_v1([-1, 0, 1, 2, -1, -4]))
print(s.threeSum_v1([-1, 0, 1, 0]))
print(s.threeSum_v1([0, 0, 0, 0]))

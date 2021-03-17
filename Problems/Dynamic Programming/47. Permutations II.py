# https://leetcode.com/problems/permutations-ii/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def dfs(cur=[], nums=nums):
            if not nums:
                res.append(cur)
                return
            pre = None
            for i, n in enumerate(nums):
                if n == pre:
                    continue
                dfs(cur+[n], nums[:i]+nums[i+1:])
                pre = n

        dfs()

        return res


s = Solution()
print(s.permuteUnique([1, 1, 2]))
print(s.permuteUnique([1, 2, 3]))

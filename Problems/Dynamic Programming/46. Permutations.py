# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(cur=[], nums=nums):
            if not nums:
                res.append(cur)
            for i, n in enumerate(nums):
                dfs(cur + [n], nums[:i] + nums[i+1:])

        dfs()

        return res

    def permute_v1(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(cur=[], canUse=[True]*len(nums)):
            if len(cur) == len(nums):
                res.append(cur)
                return

            for i, use in enumerate(canUse):
                if not use:
                    continue
                canUse[i] = False
                dfs(cur + [nums[i]], canUse)
                canUse[i] = True

        dfs()

        return res


s = Solution()
print(s.permute_v1([1, 2, 3]))

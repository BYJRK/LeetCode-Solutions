# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(target: int, idx=0, nums=[]):
            if target == 0:
                res.append(nums)
            elif target < 0:
                return
            for i in range(idx, len(candidates)):
                v = candidates[i]
                dfs(target - v, i, nums + [v])

        dfs(target)

        return res

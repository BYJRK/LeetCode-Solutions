# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def dfs(target: int, idx=0, nums=[]):
            if target == 0:
                res.append(nums)
            elif target < 0:
                return
            pre = None
            for i in range(idx, len(candidates)):
                c = candidates[i]
                if c != pre:
                    dfs(target - c, i + 1, nums + [c])
                pre = c

        dfs(target)

        return res


s = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
print(s.combinationSum2(candidates, 8))

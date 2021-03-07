# https://leetcode.com/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        # 后面的去重需要在这里保证数字按顺序排列
        nums.sort()

        def dfs(cur=[], idx=0):
            res.append(cur.copy())

            for i in range(idx, len(nums)):
                # 这里的逻辑是，如果在当前的数字（nums[idx:]）里：
                # 如果 i 在开头，则可以容忍下一个是相同的
                # 如果 i 不在开头，则跳过剩下的所有连续相同的
                # 对于 [1 2 2 2] 这种三个连续的情况
                # 第一次从 1 开始看，发现第二个相同 2 时就跳出
                # 然后下次从 2 开始看，可以容忍第一个相同的 2，但在第二个相同的 2 退出
                # 再下次从第二个 2 开始看，可以容忍第一个相同的 2
                if i > idx and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()

        dfs()

        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2, 2]))

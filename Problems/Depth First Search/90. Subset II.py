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
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(cur, i + 1)
                cur.pop()

        dfs()

        return res

    def subsetsWithDup_v2(self, nums: List[int]) -> List[List[int]]:

        res = [[]]

        nums.sort()
        pre = None
        for n in nums:
            tmp = []
            dup = dup + 1 if n == pre else 0
            for r in res:
                # 如果当前没有重复，那么直接给所有的都追加
                if not dup:
                    tmp.append(r + [n])
                    continue
                # 如果有重复（比如当前是第 k 个相同数字）
                # 那么想要追加，需要满足下列要求：
                # 要被追加的数组的倒数 (k-1) 个数字必须都是这个数
                if len(r) < dup:
                    continue
                flag = True
                for i in range(-1, -1 - dup, -1):
                    if r[i] != n:
                        flag = False
                        break
                if flag:
                    tmp.append(r + [n])
            res.extend(tmp)
            pre = n

        return res


s = Solution()
print(s.subsetsWithDup_v2([1, 2, 2, 2]))

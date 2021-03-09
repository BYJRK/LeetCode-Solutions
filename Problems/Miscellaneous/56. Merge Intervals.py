# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i: i[0])

        res = []
        tmp = None
        for r in intervals:
            if not tmp:
                tmp = r
                continue
            if r[0] <= tmp[1]:
                tmp[1] = max(tmp[1], r[1])
            else:
                res.append(tmp)
                tmp = r
        if tmp:
            res.append(tmp)

        return res

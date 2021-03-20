# https://leetcode.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        dic = {c: i for i, c in enumerate(S)}
        res = []

        checked = set()
        begin = 0
        last = 0
        for i, c in enumerate(S):
            if c not in checked:
                last = dic[c] if dic[c] > last else last
                checked.add(c)
            if i == last:
                res.append(last - begin + 1)
                begin = last = last + 1
                checked.clear()

        return res


s = Solution()
print(s.partitionLabels('ababcbacadefegdehijhklij'))

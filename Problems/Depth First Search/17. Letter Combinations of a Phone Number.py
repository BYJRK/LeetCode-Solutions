# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

dic = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        def permute(g1: List[str], g2: List[str]) -> List[str]:
            res = []
            for w1 in g1:
                for w2 in g2:
                    res.append(w1 + w2)
            return res

        res = ['']
        for d in digits:
            res = permute(res, dic[d])

        return res

    def letterCombinations_v2(self, digits: str) -> List[str]:
        def dfs(cur, index=0):
            if len(digits) == 0:
                return []
            words = dic[digits[index]]
            res = []
            for w1 in cur:
                for w2 in words:
                    res.append(w1 + w2)
            index += 1
            if index == len(digits):
                return res
            else:
                return dfs(res, index)

        return dfs([''])


s = Solution()
print(s.letterCombinations_v2('23'))

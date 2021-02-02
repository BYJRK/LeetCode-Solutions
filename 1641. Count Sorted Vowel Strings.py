# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.count(0, n)

    def count(self, v, n, memo={}):
        """
        v 指的是所有字母必须等于其或在其之后，v 是一个数字，比如 a=0，e=1，...
        n 指的是有几位
        """
        if f'{v}:{n}' in memo:
            return memo[f'{v}:{n}']
        if n == 1:
            res = 5 - v
        elif n > 1:
            res = sum([self.count(_v, n - 1) for _v in range(v, 5)])
        memo[f'{v}:{n}'] = res
        return res

s = Solution()
print(s.countVowelStrings(1))  # 5
print(s.countVowelStrings(2))  # 15
print(s.countVowelStrings(3))  # 35
print(s.countVowelStrings(33))  # 66045

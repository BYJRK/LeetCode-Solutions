# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        res = ''

        for c in s:
            res += c
            if res[-k:] == c * k:
                res = res[:-k]

        return res


s = Solution()
print(s.removeDuplicates('deeedbbcccbdaa', 3))

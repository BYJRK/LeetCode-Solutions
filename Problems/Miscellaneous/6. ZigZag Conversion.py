# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) <= numRows or numRows == 1:
            return s

        res = [''] * numRows
        dir_ = True  # True: ↓, False: ↗
        curRow = 0
        for i, c in enumerate(s):
            res[curRow] += c
            curRow += 1 if dir_ else -1
            if curRow == 0 or curRow == numRows - 1:
                dir_ = not dir_
        return ''.join(res)


s = Solution()
print(s.convert('PAYPALISHIRING', 3))
print(s.convert('PAYPALISHIRING', 4))

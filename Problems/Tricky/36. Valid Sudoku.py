# https://leetcode.com/problems/valid-sudoku/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(nums):
            checked = set()
            for n in nums:
                if n == '.':
                    continue
                if n not in checked:
                    checked.add(n)
                else:
                    return False
            return True

        # rows
        for row in board:
            if not check(row):
                return False

        # cols
        for col in range(9):
            column = [board[i][col] for i in range(9)]
            if not check(column):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = []
                block.extend(board[i][j:j+3])
                block.extend(board[i+1][j:j+3])
                block.extend(board[i+2][j:j+3])
                if not check(block):
                    return False

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s = Solution()
print(s.isValidSudoku(board))

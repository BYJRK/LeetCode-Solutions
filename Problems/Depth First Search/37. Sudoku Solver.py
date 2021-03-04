# https://leetcode.com/problems/sudoku-solver/

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(num, row, col, board) -> bool:
            '''
            检查在指定位置输入数字是否可行
            这里假定 board[row][col] == '.'，也就是当前位置是空的
            所以不需要在遍历的时候检查是否和给定位置重合
            '''
            assert board[row][col] == '.'
            for i in range(9):
                if board[row][i] == num:
                    return False
                if board[i][col] == num:
                    return False
            r0, c0 = row // 3 * 3, col // 3 * 3
            for i in range(3):
                for j in range(3):
                    r = r0 + i
                    c = c0 + j
                    if board[r][c] == num:
                        return False
            return True

        def findEmpty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i, j
            return None

        def solve(board) -> bool:
            empty = findEmpty(board)
            # 所有都填写完毕
            if not empty:
                return True
            r, c = empty
            for i in range(1, 10):
                num = str(i)
                if valid(num, r, c, board):
                    board[r][c] = num
                    # 如果就这么递归地填写下去，最终可以填满
                    if solve(board):
                        return True
                    # 否则将当前位置的数字重新设为空
                    board[r][c] = '.'

            return False

        solve(board)


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
s.solveSudoku(board)
print(board)

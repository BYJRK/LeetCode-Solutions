# https://leetcode.com/problems/n-queens/

from typing import List
from copy import deepcopy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]

        res = []

        def dfs(board: List[List[bool]], line: int = 0):
            # 如果每一行都已经填上了数字，则记录当前的结果
            if line == n:
                res.append(generate_board(board))
                return
            # 尝试把 Q 放在第 line 行 i 位置
            for i in range(n):
                flag = True
                # 检查 line 之前的每一行
                for j in range(line):
                    # 检查这一列有无冲突
                    if board[j][i]:
                        flag = False
                        break
                    # 检查对角线
                    d = line - j
                    if i - d >= 0 and board[j][i - d]:
                        flag = False
                        break
                    if i + d < n and board[j][i + d]:
                        flag = False
                        break
                if flag:
                    board[line][i] = True
                    dfs(board, line + 1)
                    board[line][i] = False

        def generate_board(rows: List[List[bool]]):
            res = []
            for row in rows:
                line = ''
                for col in row:
                    if col:
                        line += 'Q'
                    else:
                        line += '.'
                res.append(line)
            return res

        board = [[False] * n for _ in range(n)]
        dfs(board, 0)
        return res


s = Solution()
answers = s.solveNQueens(4)
for ans in answers:
    print(ans)
    print('-' * 10)

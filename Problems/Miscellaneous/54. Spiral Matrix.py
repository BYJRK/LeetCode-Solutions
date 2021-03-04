# https://leetcode.com/problems/spiral-matrix/

from typing import List
import numpy as np


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 如果其实是一维数组，则直接返回
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [m[0] for m in matrix]
        res = []
        top, left = 1, 0  # 注意初始条件，top=1
        down, right = len(matrix) - 1, len(matrix[0]) - 1
        _dir = 1  # 1: right, 2: down, 3: left, 4: up

        i, j = 0, 0
        count = len(matrix) * len(matrix[0])
        idx = 0
        while True:
            res.append(matrix[i][j])
            idx += 1
            if idx == count:
                break
            # 行走一步，如果撞墙，则换方向，并且收缩对应方向的墙
            if _dir == 1:
                j += 1
                if j == right:
                    right -= 1
                    _dir = 2
            elif _dir == 2:
                i += 1
                if i == down:
                    down -= 1
                    _dir = 3
            elif _dir == 3:
                j -= 1
                if j == left:
                    left += 1
                    _dir = 4
            elif _dir == 4:
                i -= 1
                if i == top:
                    top += 1
                    _dir = 1

        return res

    def spiralOrder_v2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            # anti-clockwise rotation
            matrix = list(zip(*matrix))[::-1]
        return res


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
s = Solution()
print(s.spiralOrder_v2(matrix1))
print(s.spiralOrder_v2(matrix2))

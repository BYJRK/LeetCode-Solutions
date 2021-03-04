# https://leetcode.com/problems/rotate-image/

import numpy as np
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l = len(matrix)
        if l == 1:
            return

        # 沿对角线翻转
        for i in range(l):
            for j in range(i + 1, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 水平翻转
        for i in range(l):
            for j in range(l // 2 + l % 2, l):
                matrix[i][j], matrix[i][l - j - 1] = \
                    matrix[i][l - j - 1], matrix[i][j]

    def rotate_v2(self, matrix: List[List[int]]) -> None:
        # clockwise
        return list(zip(*matrix[::-1]))
        # anti-clockwise
        # return list(zip(*matrix))[::-1]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(matrix))

s = Solution()
s.rotate(matrix)
print(np.array(matrix))

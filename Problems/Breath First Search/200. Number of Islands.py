# https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        count = 0

        def erode(y, x):
            if 0 <= y < rows and 0 <= x < cols and grid[y][x] == '1':
                grid[y][x] = '0'
                erode(y - 1, x)
                erode(y + 1, x)
                erode(y, x - 1)
                erode(y, x + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    erode(i, j)
                    count += 1

        return count

    def numIslands_v1(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        ones = set()
        checked = set()
        # 因为顺序并不重要，所以这里还可以用 set
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ones.add((i, j))

        def visit(y, x):
            if not 0 <= y < rows or not 0 <= x < cols:
                return
            if grid[y][x] == '1' and (y, x) not in checked:
                checked.add((y, x))
                queue.append((y, x))
                ones.remove((y, x))

        count = 0
        while ones:
            y, x = ones.pop()
            checked.add((y, x))
            queue.clear()
            queue.append((y, x))
            while queue:
                y, x = queue.popleft()
                visit(y - 1, x)
                visit(y + 1, x)
                visit(y, x - 1)
                visit(y, x + 1)
            count += 1

        return count


grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "1", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

s = Solution()
print(s.numIslands_v1(grid1))
print(s.numIslands_v1(grid2))

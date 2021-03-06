# https://leetcode.com/problems/unique-paths-iii/

from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def findPos(val):
            '''用来寻找起始和结束点'''
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == val:
                        return i, j

        start = findPos(1)
        stop = findPos(2)

        myMap = [[0] * n for _ in range(m)]
        res = 0

        def dfs(pos, curMap):
            '''尝试从当前格出发，朝着四周还没有走过的格子走下去'''

            def walkTo(i, j, curMap):
                '''走向下一个格子，并判断下一个格子能不能走'''
                if i >= 0 and i < m and j >= 0 and j < n and \
                        curMap[i][j] == 0 and grid[i][j] != -1:
                    dfs((i, j), curMap)

            def walkAll(curMap):
                '''判断是否所有能走的格子都已经走完'''
                for i in range(m):
                    for j in range(n):
                        if curMap[i][j] == 1 or grid[i][j] == -1:
                            continue
                        return False
                return True

            i, j = pos
            curMap[i][j] = 1
            # 如果已经到结束点，而且所有格子都经过了
            if pos == stop and walkAll(curMap):
                nonlocal res
                res += 1
            # 否则尝试从当前位置向四周出发
            else:
                walkTo(i - 1, j, curMap)  # 上
                walkTo(i + 1, j, curMap)  # 下
                walkTo(i, j - 1, curMap)  # 左
                walkTo(i, j + 1, curMap)  # 右

            # 要在走完后续的路并重新回来后，将当前位置设为初始值，便于以后再次经过
            curMap[i][j] = 0

        dfs(start, myMap)

        return res


grid1 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]  # 2
grid2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]  # 4
s = Solution()
print(s.uniquePathsIII(grid1))
print(s.uniquePathsIII(grid2))

# https://leetcode.com/problems/map-of-highest-peak/

from typing import List
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        h, w = len(isWater), len(isWater[0])
        res = [[-1] * w for _ in range(h)]

        countEmpty = h * w

        for i in range(h):
            for j in range(w):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    countEmpty -= 1

        curLevel = 0
        while countEmpty > 0:
            for i in range(h):
                for j in range(w):
                    if res[i][j] != curLevel:
                        continue
                    # north
                    if i > 0 and res[i - 1][j] == -1:
                        res[i - 1][j] = curLevel + 1
                        countEmpty -= 1
                    # west
                    if j > 0 and res[i][j - 1] == -1:
                        res[i][j - 1] = curLevel + 1
                        countEmpty -= 1
                    # east
                    if j < w - 1 and res[i][j + 1] == -1:
                        res[i][j + 1] = curLevel + 1
                        countEmpty -= 1
                    # south
                    if i < h - 1 and res[i + 1][j] == -1:
                        res[i + 1][j] = curLevel + 1
                        countEmpty -= 1
            curLevel += 1
            print(res)

        return res

    def highestPeak_v2(self, isWater: List[List[int]]) -> List[List[int]]:
        h, w = len(isWater), len(isWater[0])
        res = [[-1] * w for _ in range(h)]

        countEmpty = h * w
        coorsToCheck = []
        nextCoorsToCheck = []

        for i in range(h):
            for j in range(w):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    coorsToCheck.append((i, j))
                    countEmpty -= 1

        curLevel = 0
        while countEmpty > 0:
            curLevel += 1
            for i, j in coorsToCheck:
                if i > 0 and res[i - 1][j] == -1:
                    res[i - 1][j] = curLevel
                    nextCoorsToCheck.append((i - 1, j))
                    countEmpty -= 1
                # west
                if j > 0 and res[i][j - 1] == -1:
                    res[i][j - 1] = curLevel
                    nextCoorsToCheck.append((i, j - 1))
                    countEmpty -= 1
                # east
                if j < w - 1 and res[i][j + 1] == -1:
                    res[i][j + 1] = curLevel
                    nextCoorsToCheck.append((i, j + 1))
                    countEmpty -= 1
                # south
                if i < h - 1 and res[i + 1][j] == -1:
                    res[i + 1][j] = curLevel
                    nextCoorsToCheck.append((i + 1, j))
                    countEmpty -= 1
            coorsToCheck = nextCoorsToCheck
            nextCoorsToCheck = []

        return res

    def highestPeak_v3(self, isWater: List[List[int]]) -> List[List[int]]:
        h, w = len(isWater), len(isWater[0])
        res = [[-1] * w for _ in range(h)]

        countEmpty = h * w
        coorsToCheck = deque()

        for i in range(h):
            for j in range(w):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    coorsToCheck.append((i, j))
                    countEmpty -= 1

        while len(coorsToCheck) > 0:
            i, j = coorsToCheck.popleft()
            level = res[i][j] + 1
            if i > 0 and res[i - 1][j] == -1:
                res[i - 1][j] = level
                coorsToCheck.append((i - 1, j))
            # west
            if j > 0 and res[i][j - 1] == -1:
                res[i][j - 1] = level
                coorsToCheck.append((i, j - 1))
            # east
            if j < w - 1 and res[i][j + 1] == -1:
                res[i][j + 1] = level
                coorsToCheck.append((i, j + 1))
            # south
            if i < h - 1 and res[i + 1][j] == -1:
                res[i + 1][j] = level
                coorsToCheck.append((i + 1, j))

        return res


s = Solution()
m = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
print(s.highestPeak_v3(m))

# https://leetcode.com/contest/weekly-contest-265/problems/minimum-operations-to-convert-number/

from collections import deque
from operator import add, sub, xor


def minimumOperations(nums: list[int], start: int, goal: int) -> int:
    queue = deque([start])
    curCount = 1
    nxtCount = 0
    ops = [add, sub, xor]
    visited = set([start])
    step = 1
    while queue:
        if curCount > 0:
            curCount -= 1
            s = queue.popleft()
            for n in nums:
                for op in ops:
                    r = op(s, n)
                    if r == goal:
                        return step
                    if 0 <= r <= 1000 and r not in visited:
                        nxtCount += 1
                        queue.append(r)
                        visited.add(r)
        if curCount == 0:
            curCount = nxtCount
            nxtCount = 0
            step += 1
    return -1


print(minimumOperations([2, 4, 12], 2, 12))  # 2
print(minimumOperations([3, 5, 7], 0, -4))  # 2
print(minimumOperations([2, 8, 16], 0, 1))  # -1

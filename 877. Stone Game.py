# https://leetcode.com/problems/stone-game/

from typing import List
import pprint

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp_a = [[0 for _ in range(n)] for _ in range(n)]
        dp_l = [[0 for _ in range(n)] for _ in range(n)]

        def getOptScore(i: int, j: int, alexTurn: bool) -> int:
            if i > j:
                return 0
            if alexTurn:
                if dp_a[i][j] == 0:
                    dp_a[i][j] = max(piles[i] + getOptScore(i + 1, j, False),
                                     piles[j] + getOptScore(i, j - 1, False))
                return dp_a[i][j]
            else:
                if dp_l[i][j] == 0:
                    dp_l[i][j] = max(piles[i] + getOptScore(i + 1, j, True),
                                     piles[j] + getOptScore(i, j - 1, True))
                return dp_l[i][j]

        getOptScore(0, n - 1, True)
        return dp_a[0][n - 1] > sum(piles) / 2

s = Solution()
print(s.stoneGame([5, 3, 4, 5, 10, 2]))  # True

# https://leetcode.com/problems/stone-game/

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # 每一个数字表示当石堆还剩 [i, j] 范围时，能获得的最多石头
        dp_a = [[0 for _ in range(n)] for _ in range(n)]
        dp_l = [[0 for _ in range(n)] for _ in range(n)]

        def getScore(i: int, j: int, alexTurn: bool) -> int:
            if i > j:
                return 0
            if alexTurn:
                # 注意这里要加 getScore，所以互相要返回对方所能得到的最大数量
                left = piles[i] + getScore(i+1, j, False)
                right = piles[j] + getScore(i, j-1, False)
                # 根据左边或者右边哪个更优，做出选择，并返回对手在下一状态的最优
                if left > right:
                    dp_a[i][j] = left
                    return dp_l[i+1][j]
                else:
                    dp_a[i][j] = right
                    return dp_l[i][j-1]
            else:
                left = piles[i] + getScore(i+1, j, True)
                right = piles[j] + getScore(i, j-1, True)
                if left > right:
                    dp_l[i][j] = left
                    return dp_a[i+1][j]
                else:
                    dp_l[i][j] = right
                    return dp_a[i][j-1]

        getScore(0, n - 1, True)
        return dp_a[0][n - 1] > sum(piles) / 2

    def stoneGame_v1(self, piles: List[int]) -> bool:
        n = len(piles)
        # 每一个数字表示当石堆还剩 [i, j] 范围时，能获得的最多石头
        dp = [[0 for _ in range(n)] for _ in range(n)]

        def getScore(i: int, j: int) -> int:
            if i > j:
                return 0
            # 不需要再考虑是谁的回合了，因为这一信息暗含在 i,j 当中，绝对不会混淆
            left = piles[i] + getScore(i+1, j)
            right = piles[j] + getScore(i, j-1)
            # 根据左边或者右边哪个更优，做出选择，并返回对手在下一状态的最优状态
            if left > right:
                dp[i][j] = left
                return dp[i+1][j]
            else:
                dp[i][j] = right
                return dp[i][j-1]

        getScore(0, n - 1)
        return dp[0][n - 1] > sum(piles) / 2

    def stoneGame_v2(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        def getScore(i: int, j: int) -> int:
            if i > j:
                return 0
            dp[i][j] = max(piles[i] + getScore(i + 1, j),
                           piles[j] + getScore(i, j - 1))
            return dp[i][j]

        getScore(0, n - 1)
        return dp[0][n - 1] > sum(piles) / 2

    def stoneGame_v3(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = piles[i]
                else:
                    dp[i][j] = max(piles[i] - dp[i+1][j],
                                   piles[j] - dp[i][j-1])

        return dp[0][-1] > 0


s = Solution()
print(s.stoneGame_v1([5, 10, 2]))  # True
print(s.stoneGame_v1([5, 3, 4, 5, 10, 2]))  # True

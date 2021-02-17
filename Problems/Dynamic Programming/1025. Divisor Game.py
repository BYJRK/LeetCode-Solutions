# https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, N: int) -> bool:
        # return self.recursive(N, True)
        return self.dynamicProgramming(N)

    def recursive(self, N: int, isAliceTurn: bool, memo={}) -> bool:
        tag = f'{N}:{isAliceTurn}'
        if tag in memo:
            return memo[tag]
        # 如果已经是 1，则根据当前是否为 Alice 的回合来决定输赢
        if N == 1:
            return not isAliceTurn
        # 否则遍历所有可以选择的数字
        # 如果当前回合是 Alice，且存在可以赢的情况，则判定 Alice 胜利
        # 如果当前回合不是 Alice，且存在可以输的情况，则判定 Alice 失败
        for i in range(1, N):
            if N % i == 0:
                if isAliceTurn:
                    if self.recursive(N - i, not isAliceTurn):
                        memo[f'{N - i}:{not isAliceTurn}'] = True
                        return True
                else:
                    if not self.recursive(N - i, not isAliceTurn):
                        memo[f'{N - i}:{not isAliceTurn}'] = False
                        return False

        # 如果当前回合的玩家找不到获胜的方法，则判定对方胜利
        memo[f'{N}:{isAliceTurn}'] = not isAliceTurn
        return not isAliceTurn

    def dynamicProgramming(self, N: int) -> bool:
        # 表示在某个玩家的回合，N 为数组角标的时候，该玩家能否胜利
        dp_a = [False] * (N + 1)
        dp_b = [False] * (N + 1)
        # 这里稍微修改一下游戏规则（其实是等价的）
        # 假设最后的 1 也是可以拿的，而且谁拿谁输
        # 那么，N=0 的时候，是谁的回合，谁就获胜
        dp_a[0] = dp_b[0] = True

        for cur in range(2, N + 1):
            # 挑选一个当前 N 的因数
            for n in range(1, cur):
                if cur % n != 0:
                    continue
                sub = cur - n
                if dp_b[sub] == False:
                    dp_a[cur] = True
                if dp_a[sub] == False:
                    dp_b[cur] = True

        return dp_a[-1]


s = Solution()
# print(s.divisorGame(2))  # True
# print(s.divisorGame(3))  # False

# print(s.divisorGame(10))

# 通过观察结果不难发现，只要 N 是 2 的倍数，则 Alice 必胜
print(' '.join(str(s.divisorGame(r)) for r in range(1, 10)))

# print(s.divisorGame(100))

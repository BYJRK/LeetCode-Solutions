# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] 表示 word1[:i] 到 word2[:j] 的最短编辑距离
        # (i,j) 对应 word1[i-1] 和 word2[j-1]
        # 横向是 word2，纵向是 word1
        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(dp)):
            dp[i][0] = i
        for i in range(len(dp[0])):
            dp[0][i] = i

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # 各自去掉末尾
                replace = dp[i-1][j-1]
                # word1 去掉末尾，也就是对 word1 进行 delete
                delete = dp[i-1][j]
                # word2 去掉末尾，相当于对 word1 进行 insert
                insert = dp[i][j-1]
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = replace
                else:
                    dp[i][j] = min(insert, replace, delete) + 1

        return dp[-1][-1]


s = Solution()
print(s.minDistance('aaabaaa', 'aaacccbcccaaa'))  # 插入 6 个 c，所以是 6
print(s.minDistance('horse', 'zros'))  # 删除 o e，将 h 替换为 z，插入 o，所以是 4
print(s.minDistance('ephrem', 'benyam'))  # 5
print(s.minDistance('zoologicoarchaeologist', 'zoogeologist'))  # 10

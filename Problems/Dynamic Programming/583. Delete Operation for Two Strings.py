# https://leetcode.com/problems/delete-operation-for-two-strings/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word2) + 1):
            dp[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # 如果当前的两个字符是相同的，那么直接取左上角
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 否则从左和上选一个最小的，加 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]


s = Solution()
print(s.minDistance('sea', 'eat'))
print(s.minDistance('leetcode', 'etco'))

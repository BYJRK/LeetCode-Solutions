# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        # dp[i][j] 表示 s[i:j+1] 是否为回文
        dp = [[False] * l for _ in range(l)]

        longestSubstr = s[0]

        # 因为 (i, j) 是基于 (i+1, j-1) 得到的
        # 所以 i 需要倒序，确保计算 dp[i] 时 dp[i + 1] 已经计算过

        for i in range(l - 1, -1, -1):
            for j in range(i, l):
                if s[i] != s[j]:
                    continue
                if j - i <= 1:
                    dp[i][j] = True
                # 如果当前子字符串的首尾相同，则检查其去掉首尾的子字符串是否为回文
                elif dp[i + 1][j - 1]:
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > len(longestSubstr):
                    longestSubstr = s[i:j + 1]

        return longestSubstr


s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('aaaaab'))

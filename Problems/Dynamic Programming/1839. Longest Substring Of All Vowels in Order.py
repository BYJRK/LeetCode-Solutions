# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        dp = [0] * len(word)
        dic = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        dp[0] = 1 if word[0] == 'a' else 0
        for i in range(1, len(word)):
            if 0 <= dic[word[i]] - dic[word[i - 1]] <= 1 and dp[i - 1] > 0:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1 if word[i] == 'a' else 0
        res = [v for i, v in enumerate(dp) if word[i] == 'u']
        return max([v for i, v in enumerate(dp) if word[i] == 'u'], default=0)


s = Solution()
print(s.longestBeautifulSubstring('uuuuu'))  # 0
print(s.longestBeautifulSubstring('aeiaaioaaaaeiiiiouuuooaauuaeiu'))  # 13
print(s.longestBeautifulSubstring('aeeeiiiioooauuuaeiou'))  # 5

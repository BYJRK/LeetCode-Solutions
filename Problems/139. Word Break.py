# https://leetcode.com/problems/word-break/

from typing import List


class Solution:
    def wordBreak_v1(self, s: str, wordDict: List[str]) -> bool:
        """
        dp 的 tabulation 方法一
        """

        # dp[i] 表示 s 的前 i 个字符（s[0:i]）可以被分割（i 从 1 开始计）
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            # 如果前 i 个字符在字典中，则表明前 i 个字符可以被分割
            if s[:i] in wordDict:
                dp[i] = True
            # 否则的话，在前 i 个字符中寻找一个位置 j
            # 如果前 j 个字符可以被分割，且 j 之后的字符在字典中
            # 则表明前 i 个字符可以被分割
            else:
                for j in range(i):
                    # dp[j] 意思是前 j 个字符（s[:j]）可以被分割
                    if dp[j] and s[j:i] in wordDict:
                        dp[i] = True

        return dp[-1]

    def wordBreak_v2(self, s: str, wordDict: List[str]) -> bool:
        """
        dp 的 tabulation 方法二
        """

        dp = [True] + [False] * len(s)

        for i in range(len(s) + 1):
            if not dp[i]:
                continue
            tmp = s[i:]
            for w in wordDict:
                if tmp.startswith(w):
                    idx = i + len(w)
                    if idx <= len(s):
                        dp[idx] = True

        return dp[-1]

    def wordBreak_v3(self, s: str, wordDict: List[str]) -> bool:
        """
        dp 的 memoization 方法
        """

        def canBreak(s: str, memo={}) -> bool:
            """
            递归调用
            """
            if s in memo:
                return memo[s]

            # 如果长度为零，则认为一定可以分割
            if len(s) == 0:
                return True

            memo[s] = False
            # 遍历词典中的每个词，找到一个符和字符串开头规律的
            # 然后将字符串与这个词相同的开头去掉，并判断字符串剩下的部分是否也能被分割
            for w in wordDict:
                if s.startswith(w):
                    if canBreak(s[len(w):], memo):
                        memo[s] = True
                        break

            return memo[s]

        return canBreak(s)

s = Solution()
print(s.wordBreak_v3('applepenapple', ["apple", "pen"]))  # True
print(s.wordBreak_v3('catsandog', ["cats", "dog", "sand", "and", "cat"])) # False

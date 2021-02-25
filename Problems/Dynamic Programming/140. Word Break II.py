# https://leetcode.com/problems/word-break-ii/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # 做一个快速的检查，如果 s 中存在所有 word 都不包含的字母，则直接退出
        set1 = set(s)
        set2 = set(''.join(wordDict))
        if not set1.issubset(set2):
            return []

        # dp[i] 的意思是，子字符串 s[:i] 能以怎样的方式进行分割
        # 如果是 [[]] 则表示开头
        # 如果是 [None]，则表示还没有访问到，或没有办法进行分割
        # 如果是 [['a', 'b'], ['ab']] 则表示目前已经有两种方式拼出这个子字符串
        dp = [None] * (len(s) + 1)
        dp[0] = [[]]

        for i in range(len(s) + 1):
            # 如果当前子字符串无法分割，则跳过
            if dp[i] is None:
                continue
            tmp = s[i:]
            for w in wordDict:
                idx = len(w) + i
                if idx > len(s):
                    continue
                if tmp.startswith(w):
                    if dp[idx] is None:
                        dp[idx] = []
                    # 将目前的所有方式全部添加到新的位置，并在每个的最后追加当前的单词
                    for dic in dp[i]:
                        dp[idx].append(dic + [w])

        if dp[-1] is None:
            return []
        return [' '.join(res) for res in dp[-1]]

    def wordBreak_dfs(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(s: str, memo={}):
            if s in memo:
                return memo[s]
            if len(s) == 0:
                return [[]]

            res = []
            for w in wordDict:
                if s.startswith(w):
                    tmp = s[len(w):]
                    combos = dfs(tmp, memo)
                    for combo in combos:
                        res.append([w] + combo)

            memo[s] = res

            return res

        return dfs(s)


s = Solution()

print(s.wordBreak_dfs('catsanddog', ["cat", "cats", "and", "sand", "dog"]))

print(s.wordBreak_dfs('pineapplepenapple', [
      "apple", "pen", "applepen", "pine", "pineapple"]))

# text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
#          "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

# print(s.wordBreak(text, words))

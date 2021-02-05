# https://leetcode.com/problems/longest-string-chain/

from typing import List


class Solution:
    def longestStrChain_v1(self, words: List[str]) -> int:
        l = len(words)
        res = dict(zip(words, [1] * l))
        words.sort(key=len)

        def isPred(w1, w2):
            if len(w2) - len(w1) != 1:
                return False
            for i in range(len(w2)):
                if w1 == w2[:i] + w2[i + 1:]:
                    return True
            return False

        for i in range(l):
            for j in range(i + 1, l):
                w1, w2 = words[i], words[j]
                if isPred(w1, w2):
                    res[w2] = max(res[w2], res[w1] + 1)

        return max(res.values())

    def longestStrChain_v2(self, words: List[str]) -> int:
        l = len(words)
        res = dict(zip(words, [1] * l))
        words.sort(key=len)

        for w in words:
            for i in range(len(w)):
                c = w[:i] + w[i + 1:]
                if c in res:
                    res[w] = max(res[w], res[c] + 1)

        return max(res.values())


s = Solution()
print(s.longestStrChain_v1(["a", "b", "ba", "bca", "bda", "bdca"]))  # 4
print(s.longestStrChain_v1(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))  # 5
print(s.longestStrChain_v2(["a", "b", "ba", "bca", "bda", "bdca"]))  # 4
print(s.longestStrChain_v2(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))  # 5

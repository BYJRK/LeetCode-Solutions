class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def findLongest(s: str) -> str:
            if len(s) < 2:
                return ''
            # 先找出所有 not nice 的字符的位置
            pivots = []
            for i, c in enumerate(s):
                if c.islower() and c.upper() not in s or \
                    c.isupper() and c.lower() not in s:
                    pivots.append(i)
            # 如果没找到，那当前字符串就是最长的
            if not pivots:
                return s
            # 如果找到的和总长度一样多，那不存在
            if len(pivots) == len(s):
                return ''
            # 分治法
            p = pivots[len(pivots) // 2]
            return max(findLongest(s[:p]), findLongest(s[p + 1:]), key=len)

        return findLongest(s)


s = Solution()
# print(s.longestNiceSubstring(('dDzeE')))
print(s.longestNiceSubstring(('YazaAay')))

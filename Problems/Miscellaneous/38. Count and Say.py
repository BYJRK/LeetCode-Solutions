# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)
        res = []
        count = 0
        pre = ''
        for c in s:
            # 如果是开头第一个，或者跟上一个一样，则计数
            if not pre or c == pre:
                count += 1
            # 否则将目前计出的数字“念出来”
            else:
                res += [str(count), pre]
                # 因为已经移到了新的数字上，所以 count=1
                count = 1
            pre = c
        res += [str(count), pre]
        return ''.join(res)


s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))

# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def str2int(s: str) -> int:
            res = 0
            for i, c in enumerate(reversed(s)):
                res += (ord(c) - 48) * 10 ** i
            return res

        def int2str(n: int) -> str:
            if n == 0:
                return '0'
            digits = []
            while n > 0:
                rem = n % 10
                n //= 10
                digits.append(chr(rem + 48))
            return ''.join(reversed(digits))

        return int2str(str2int(num1) * str2int(num2))


s = Solution()
print(s.multiply('123', '456'))

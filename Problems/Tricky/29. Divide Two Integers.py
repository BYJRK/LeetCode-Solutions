# https://leetcode.com/problems/divide-two-integers/

from typing import Tuple


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        def doDivision(num1: int, num2: int) -> Tuple[int, int]:
            '''用减法实现除法，假定两个数字都是正数'''
            assert num1 >= 0 and num2 >= 0
            res = 0
            while num1 >= num2:
                res += 1
                num1 -= num2
            return res, num1

        # 判断是否为负数
        isNagetive = False
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            isNagetive = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        ans = ''
        numstr = str(dividend)
        idx = 0
        carry = ''
        while len(numstr) > 0:
            num = int(carry + numstr[:idx + 1])
            if num < divisor:
                idx += 1
                ans += '0'
                if idx == len(numstr):
                    break
                continue
            res, rem = doDivision(num, divisor)
            ans += str(res)
            carry = str(rem)
            numstr = numstr[idx + 1:]
            idx = 0

        ans = int(ans.lstrip('0'))
        if isNagetive:
            ans = -ans
        return min(ans, 2 ** 31 - 1)


s = Solution()
print(s.divide(0, 21))
print(s.divide(12345, 21))
print(s.divide(2147483647, 2))
print(s.divide(-1060849722, 99958928))
print(s.divide(-1106478492, 36592642))

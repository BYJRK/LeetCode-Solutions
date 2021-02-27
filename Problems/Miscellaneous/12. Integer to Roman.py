# https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = ''

        for key, value in reversed(dic.items()):
            c = num // value
            if c == 4:
                if key == 'I':
                    if res and res[-1] == 'V':
                        res = res[:-1] + 'IX'
                    else:
                        res += 'IV'
                elif key == 'X':
                    if res and res[-1] == 'L':
                        res = res[:-1] + 'XC'
                    else:
                        res += 'XL'
                elif key == 'C':
                    if res and res[-1] == 'D':
                        res = res[:-1] + 'CM'
                    else:
                        res += 'CD'
            else:
                res += key * c
            num -= c * value

        return res

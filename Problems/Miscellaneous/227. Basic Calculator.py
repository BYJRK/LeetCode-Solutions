# https://leetcode.com/problems/basic-calculator-ii/


from re import template


class Solution:
    def calculate(self, s: str) -> int:

        ops = set('+-*/')

        stack = []

        tmp = ''
        op = '+'
        for i, c in enumerate(s):
            if c.isspace():
                continue
            elif c.isdigit():
                tmp += c
                if i < len(s) - 1:
                    continue
            if c in ops or i == len(s) - 1:
                num = int(tmp)
                tmp = ''
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    stack[-1] = int(stack[-1] / num)
                op = c

        return sum(stack)


s = Solution()
# print(s.calculate('10 - 4 + 3 * 2 + 10 / 5'))
# print(s.calculate('3 / 2'))
print(s.calculate('14-3 / 2'))

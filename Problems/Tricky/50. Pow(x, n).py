# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def func(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n % 2 == 0:
                return func(x * x, n // 2)
            else:
                # n = 5，x^5 = x * x^(5-1) = x * (x * x)^((5-1)/2)
                # n = 1，x^1 = x * x^(1-1) = x * (x * x)^0 = x
                # return x * func(x * x, )
                return x * func(x * x, (n - 1) // 2)

        ans = func(x, abs(n))
        if n < 0:
            ans = 1 / ans
        return ans


s = Solution()
print(s.myPow(2, 10))
print(s.myPow(2.1, 3))
print(s.myPow(2, -1))

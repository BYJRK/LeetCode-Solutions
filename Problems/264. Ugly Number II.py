# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        index = [0, 0, 0]
        number = [2, 3, 5]
        for _ in range(n):
            tmp = [res[index[j]] * number[j] for j in range(3)]
            res.append(min(tmp))
            for j in range(3):
                if tmp[j] == res[-1]:
                    index[j] += 1
        return res[n-1]


s = Solution()
print(s.nthUglyNumber(10))  # 12

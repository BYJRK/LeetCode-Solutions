# https://leetcode.com/problems/ugly-number-ii/

import heapq


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
        return res[n - 1]

    def nthUglyNumber_v1(self, n: int) -> int:
        dp = [1] + [0] * (n-1)
        p2 = p3 = p5 = 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[-1]

    def nthUglyNumber_v2(self, n: int) -> int:
        heap = [1]
        ans = []
        seen = set()
        while len(ans) < n:
            h = heapq.heappop(heap)
            ans.append(h)
            a, b, c = 2 * h, 3 * h, 5 * h
            if a not in seen:
                seen.add(a)
                heapq.heappush(heap, a)
            if b not in seen:
                seen.add(b)
                heapq.heappush(heap, b)
            if c not in seen:
                seen.add(c)
                heapq.heappush(heap, c)
        return ans[-1]


#    2 3 5
# 1  0 0 0
# 2  1 0 0
# 3  0 1 0
# 4  2 0 0
# 5  0 0 1
# 6  1 1 0
# 8  3 0 0
# 9  0 2 0
# 10 1 0 1
s = Solution()
print(s.nthUglyNumber_v2(10))  # 12
print(s.nthUglyNumber_v2(100))  # 1536

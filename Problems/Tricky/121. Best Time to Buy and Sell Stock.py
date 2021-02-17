# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        O(n) 时间复杂度

        大致思路：
        从左到右，记录两个值
        1. 当前最小的数字 min_num
        2. 当前的最大利润 max_pft

        然后遍历整个 prices 数组，令某个数字为 p：
        1. 如果发现了更小的数字（即 p < min_num），则更新 min_num
        2. 如果发现 (p - min_num) > max_pft，则更新 max_pft

        假如最大的利益在前半部分，那么即便在后面找到了更小的数字，
        但是 max_pft 不会受到影响
        """
        l = len(prices)
        if l == 1:
            return 0
        elif l == 2:
            return max(prices[1] - prices[0], 0)

        min_num = prices[0]
        max_pft = 0
        for p in prices[1:]:
            if p < min_num:
                min_num = p
            elif p - min_num > max_pft:
                max_pft = p - min_num

        return max(max_pft, 0)

    def maxProfit_bf(self, prices: List[int]) -> int:
        """
        O(n^2) 时间复杂度
        """
        l = len(prices)
        if l == 1:
            return 0
        elif l == 2:
            return max(prices[1] - prices[0], 0)

        _max = -100000
        for i in range(l):
            for j in range(i + 1, l):
                if prices[j] - prices[i] > _max:
                    _max = prices[j] - prices[i]

        return max(_max, 0)


s = Solution()
print(s.maxProfit([1, 4, 2]))  # 3
print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
print(s.maxProfit([7, 6, 4, 3, 1]))  # 0

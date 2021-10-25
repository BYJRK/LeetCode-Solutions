from typing import List
import heapq


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys = []
        sells = []
        for price, amount, _type in orders:
            # buy, look for smallest sell
            if _type == 0:
                while sells and amount > 0:
                    p, a = sells[0]
                    if p <= price:
                        if a <= amount:
                            amount -= a
                            heapq.heappop(sells)
                        else:
                            sells[0][1] -= amount
                            amount = 0
                    else:
                        break
            # sell, look for largest buy
            else:
                while buys and amount > 0:
                    p, a = buys[0]
                    if -p >= price:
                        if a <= amount:
                            amount -= a
                            heapq.heappop(buys)
                        else:
                            buys[0][1] -= amount
                            amount = 0
                    else:
                        break
            if amount > 0:
                if _type == 0:
                    heapq.heappush(buys, [-price, amount])
                else:
                    heapq.heappush(sells, [price, amount])
        return (sum([b[1] for b in buys]) + \
                sum([s[1] for s in sells])) % int(1e9 + 7)


s = Solution()
log1 = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
log2 = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
print(s.getNumberOfBacklogOrders(log1))
print(s.getNumberOfBacklogOrders(log2))

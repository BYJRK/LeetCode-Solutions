from sortedcontainers import SortedList
import heapq


class MedianFinder_1:

    def __init__(self):
        self.lst = SortedList()

    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        l = len(self.lst)
        if l % 2 == 1:
            return float(self.lst[l // 2])
        else:
            return sum(self.lst[l//2-1:l//2+1]) / 2


class MedianFinder_2:

    def __init__(self):

        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        # min 只可能在刚开始是空的，之后至少会有一个
        if len(self.min) == 0:
            heapq.heappush(self.min, num)
        # 如果新的数字比 min 最小的还要小，那就放在 max 里
        elif num <= self.min[0]:
            heapq.heappush(self.max, -num)
        # 否则的话，将 min 最小的放到 max 里，然后把新的放到 min 里
        # 这样能保证 min[0] >= max[0]
        else:
            heapq.heappush(self.max, -heapq.heappop(self.min))
            heapq.heappush(self.min, num)

        # 最后，如果两个堆的数量不平均，则进行相关调整，使数量差 <= 1
        while len(self.min) - len(self.max) >= 2:
            heapq.heappush(self.max, -heapq.heappop(self.min))
        while len(self.max) - len(self.min) >= 2:
            heapq.heappush(self.min, -heapq.heappop(self.max))

    def findMedian(self) -> float:
        if (len(self.min) + len(self.max)) % 2 == 1:
            if (len(self.min) > len(self.max)):
                return self.min[0]
            else:
                return -self.max[0]
        else:
            return (self.min[0] - self.max[0]) / 2


s = MedianFinder_2()
s.addNum(1)
print(s.findMedian())
s.addNum(2)
print(s.findMedian())
s.addNum(2)
print(s.findMedian())

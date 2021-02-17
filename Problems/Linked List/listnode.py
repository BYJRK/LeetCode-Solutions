from __future__ import annotations
from typing import List


class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

    @staticmethod
    def create(*nums: List[int]) -> ListNode:
        head = ListNode(nums[0])
        p = head
        for n in nums[1:]:
            p.next = ListNode(n)
            p = p.next
        return head

    def tolist(self) -> List[int]:
        l = []
        p = self
        while p != None:
            l.append(p.val)
            p = p.next
        return l

    @staticmethod
    def display(node: ListNode) -> None:
        print(', '.join([str(n) for n in node.tolist()]))

# https://leetcode.com/problems/linked-list-cycle/description/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle_v1(self, head: ListNode) -> bool:
        """
        传统思路，循环一遍，每次都做一个标记
        """
        p = head
        while p != None:
            if not hasattr(p, 'check'):
                p.check = True
            elif p.check:
                return True
            p = p.next
        return False

    def hasCycle_v2(self, head: ListNode) -> bool:
        """
        快慢指针
        """
        p1 = head
        p2 = head
        while p1 != None and p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

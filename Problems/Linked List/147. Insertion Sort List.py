# https://leetcode.com/problems/insertion-sort-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        res = ListNode(0)
        p1 = head
        while p1 != None:
            val = p1.val
            pre = res
            p2 = res.next
            while p2 != None and val > p2.val:
                pre = p2
                p2 = p2.next

            pre.next = ListNode(p1.val)
            pre.next.next = p2

            p1 = p1.next
        return res.next


l = ListNode(4, ListNode(2, ListNode(3, ListNode(1))))
s = Solution()
s.insertionSortList(l)

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
        p_ori = head
        while p_ori != None:
            pre = res
            p_res = res.next
            while p_res != None and p_ori.val > p_res.val:
                pre = p_res
                p_res = p_res.next

            pre.next = ListNode(p_ori.val)
            pre.next.next = p_res

            p_ori = p_ori.next
        return res.next


l = ListNode(4, ListNode(2, ListNode(3, ListNode(1))))
s = Solution()
s.insertionSortList(l)

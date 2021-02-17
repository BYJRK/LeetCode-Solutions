# https://leetcode.com/problems/merge-two-sorted-lists/

from listnode import ListNode


class Solution:
    def mergeTwoLists_v1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        传统思路：创建一个新的链表，存储结果
        '''
        head = ListNode()
        p = head
        while True:
            if l1.val < l2.val:
                v = l1.val
                l1 = l1.next
            else:
                v = l2.val
                l2 = l2.next
            p.val = v
            if l1 == None:
                p.next = l2
                break
            elif l2 == None:
                p.next = l1
                break
            else:
                p.next = ListNode()
                p = p.next

        return head

    def mergeTwoLists_v2(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        递归思想
        '''
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists_v2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_v2(l1, l2.next)
            return l2


s = Solution()
n1 = ListNode.create(1, 4, 7)
n2 = ListNode.create(4, 5, 6)
ListNode.display(s.mergeTwoLists_v1(n1, n2))
ListNode.display(s.mergeTwoLists_v2(n1, n2))

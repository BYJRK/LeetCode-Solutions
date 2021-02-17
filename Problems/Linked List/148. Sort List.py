# https://leetcode.com/problems/sort-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        首先判断长度
        如果长度小于 2，则不需要排序，直接返回
        '''
        if head == None or head.next == None:
            return head

        '''
        然后获取中间点
        这一步略微不同于 876 题，对于中点的选择没有那么严格的要求
        找到中间点之后，将当前链表一分为二（中间断开）
        '''
        p = self.middleNode(head)
        mid = p.next
        p.next = None  # 断开

        '''
        然后对于左右两边，分别再进行拆分
        '''
        left = self.sortList(head)
        right = self.sortList(mid)

        '''
        最后将左右两边进行合并
        '''
        return self.mergeTwoLists(left, right)

    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head
        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next
        return p1

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

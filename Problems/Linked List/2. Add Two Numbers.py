# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        carry = 0
        cur = ListNode()
        res = cur
        while True:
            tmp = 0
            if p1 != None:
                tmp += p1.val
                p1 = p1.next
            if p2 != None:
                tmp += p2.val
                p2 = p2.next
            tmp += carry
            carry = tmp // 10
            cur.val = tmp % 10
            if p1 != None or p2 != None or carry != 0:
                cur.next = ListNode()
                cur = cur.next
            # 当两个链表均到达末尾，且没有进位时，结束循环
            else:
                break
        return res

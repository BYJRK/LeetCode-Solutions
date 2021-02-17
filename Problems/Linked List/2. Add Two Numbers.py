# https://leetcode.com/problems/add-two-numbers/

from listnode import ListNode


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

    def printNumber(self, node: ListNode) -> None:
        res = []
        p = node
        while p != None:
            res.insert(0, p.val)
            p = p.next
        print(''.join([str(c) for c in res]))


n1 = ListNode.create(2, 4, 3)
n2 = ListNode.create(5, 6, 4)
n3 = ListNode(1)
n4 = ListNode.create(9, 9, 9, 9)

s = Solution()
s.printNumber(s.addTwoNumbers(n1, n2))
s.printNumber(s.addTwoNumbers(n3, n4))

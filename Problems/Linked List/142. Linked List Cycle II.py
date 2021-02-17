# https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        快慢指针

        设 head 到 cycle 起点 C 距离为 x1
        C 到 相遇点 M 距离为 x2
        M 继续向前到 C 距离为 x3
        则相遇时，慢指针路程 x1+x2，快指针路程 x1+x2+x3+x2=2(x1+x2)，得 x1=x3
        也就是说，在相遇时，慢指针继续往前走，同时快指针回到 head 并以同样的速度移动
        两指针会在 C 点相遇（一个走了 x1，一个走了 x3）
        """
        p1 = head
        p2 = head
        while p1 != None and p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p2 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p2
        return None

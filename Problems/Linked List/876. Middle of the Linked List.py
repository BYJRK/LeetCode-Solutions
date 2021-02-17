# https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        """
        快慢指针的方法，快指针速度是 2，且到结尾时，慢指针指向中间
        """
        p1 = head
        p2 = head

        while p2.next != None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next

        # 此时有两种情况：
        # 如果总数是奇数，比如 1 2 3 4 5，此时快指向 5，慢指向 3，则慢直接就是结果
        if p2.next == None:
            return p1
        # 如果是偶数，比如 1 2 3 4 5 6，此时快指向 5，慢指向 3，则慢的下一个是结果
        else:
            return p1.next

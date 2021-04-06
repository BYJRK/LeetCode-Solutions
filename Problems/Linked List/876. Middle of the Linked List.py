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

    def middleNode_v1(self, head: ListNode) -> ListNode:
        """
        传统方法，先遍历一遍，计算长度，然后第二遍找中点
        """
        length = 1
        p = head
        while p.next != None:
            p = p.next
            length += 1

        p = head
        for _ in range(length // 2):
            p = p.next

        return p


def create_list(*nums):
    head = ListNode()
    p = head
    for n in nums:
        p.next = ListNode()
        p = p.next
        p.val = n
    return head.next


list1 = create_list(1, 2, 3, 4, 5, 6, 7)
list2 = create_list(1, 2, 3, 4, 5, 6, 7, 8)
s = Solution()
print(s.middleNode(list1).val)
print(s.middleNode(list2).val)

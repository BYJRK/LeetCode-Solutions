# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1 = None
        while head != None:
            p2 = ListNode(head.val, p1)
            p1 = p2
            head = head.next
        return p1

    def reverseList_v1(self, head: ListNode) -> ListNode:

        def func(node: ListNode) -> ListNode:
            # 如果是空，或者指向空，则什么也不做
            if node is None or node.next is None:
                return node
            # 对之后的链表进行翻转
            p = func(node.next)
            # 让下一个指向自己，并让自己指向空
            node.next.next = node
            node.next = None
            # 此时返回的是原本链表的尾，现在成了头
            return p

        return func(head)


def display(node: ListNode):
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    print(', '.join([str(r) for r in res]))


link = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
s = Solution()
display(link)
link = s.reverseList_v1(link)
display(link)

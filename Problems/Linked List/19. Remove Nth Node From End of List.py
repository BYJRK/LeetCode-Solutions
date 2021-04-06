# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd_v1(self, head: ListNode, n: int) -> ListNode:
        '''
        传统思路：
        先遍历一遍，统计数量
        然后第二遍找到倒数第 n 个并删掉
        '''
        p = head
        length = 0
        while p != None:
            p = p.next
            length += 1
        p = head
        pre = p
        n = length - n
        # 如果要删除的是头节点，则特殊对待
        if n == 0:
            return head.next
        i = 0
        while i != n:
            pre = p
            p = p.next
            i += 1
        pre.next = p.next
        return head

    def removeNthFromEnd_v2(self, head: ListNode, n: int) -> ListNode:
        """
        快慢指针，快指针先出发 n 步，然后慢指针跟上
        快指针到达结尾的时候，慢指针正好指向倒数第 n 个的前一个
        """
        # pf = head
        # ps = head
        # idx = 0
        # while pf != None:
        #     pf = pf.next
        #     pre = ps
        #     if idx >= n:
        #         ps = ps.next
        #     idx += 1
        # if ps == head:
        #     head = head.next
        # else:
        #     pre.next = ps.next
        # return head
        p1 = head
        p2 = head
        for _ in range(n - 1):
            p2 = p2.next
        while p2.next != None:
            pre = p1
            p1 = p1.next
            p2 = p2.next
        # 如果此时慢指针就是头指针，则特殊对待
        if p1 == head:
            return p1.next
        pre.next = p1.next
        return head


def create_list(*nums):
    head = ListNode()
    p = head
    for n in nums:
        p.next = ListNode()
        p = p.next
        p.val = n
    return head.next


def display_list(node: ListNode):
    p = node
    res = []
    while p != None:
        res.append(p.val)
        p = p.next
    print(', '.join([str(v) for v in res]))


list1 = create_list(1, 2, 3, 4, 5, 6, 7)
display_list(list1)
s = Solution()
display_list(s.removeNthFromEnd_v2(list1, 7))

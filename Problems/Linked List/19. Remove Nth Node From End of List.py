# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from listnode import ListNode


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
        prev = p
        n = length - n
        # 如果要删除的是头节点，则特殊对待
        if n == 0:
            return head.next
        i = 0
        while i != n:
            prev = p
            p = p.next
            i += 1
        prev.next = p.next
        return head


s = Solution()
l = ListNode.create(1, 2, 3, 4, 5)
l = s.removeNthFromEnd_v1(l, 5)
ListNode.display(l)

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/


from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return None

        def findMiddle(head: ListNode) -> ListNode:
            # p1、p2 为快慢指针
            # pre 为 p1 的上一个点
            p1 = p2 = pre = head

            while p2.next != None and p2.next.next != None:
                p2 = p2.next.next
                pre = p1
                p1 = p1.next
            # 说明 p1 完全没有移动，也就是 head 是中点
            if pre == p1:
                pre = None
            return pre, p1

        def toTree(left: ListNode, right: ListNode) -> TreeNode:
            # 说明这一侧只有一个数字
            if left == right:
                return TreeNode(left.val)
            # 说明之前的右侧已经没有了
            if left == None:
                return None
            # 说明之前的左侧已经没有了
            if right == None:
                return None

            # 断开右边的链
            right.next = None
            pre, mid = findMiddle(left)

            return TreeNode(mid.val, toTree(left, pre), toTree(mid.next, right))

        # 找到结尾
        tail = head
        while tail.next != None:
            tail = tail.next
        return toTree(head, tail)


s = Solution()
lst = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
s.sortedListToBST(lst)
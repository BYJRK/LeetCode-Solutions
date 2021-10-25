# https://leetcode.com/problems/lru-cache/


class ListNode:
    """
    自己实现一个 ListNode，而不是使用 Python 的 deque
    是因为后者不能实现给定指针并以 O(1) 的效率删除一个元素
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_head(self, key):
        """将 node 移动到 head"""
        node = self.hashmap[key]
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        _next.prev = _prev

        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        return node.value

    def pop_tail(self):
        """删除链表结尾的元素"""
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        self.hashmap.pop(last.key)
        return last.value

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        return self.move_to_head(key)

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_to_head(key)
            return
        # 如果超出容量，则删除最后一个
        if len(self.hashmap) >= self.capacity:
            self.pop_tail()

        node = ListNode(key, value)
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.hashmap[key] = node


# Q1
lru = LRUCache(2)
print(lru.get(2))
print(lru.put(2, 6))
print(lru.get(1))
print(lru.put(1, 5))
print(lru.put(1, 2))
print(lru.get(1))
print(lru.get(2))

print('-' * 20)

# Q2
lru = LRUCache(2)
print(lru.put(2, 1))
print(lru.put(2, 2))
print(lru.get(2))
print(lru.put(1, 1))
print(lru.put(4, 1))
print(lru.get(2))
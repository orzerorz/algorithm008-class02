#!/usr/bin/env python
"""
基于双指针+数组 实现的 双端队列 时间复杂度 增删 O(1),查询 O(n);空间复杂度 O(n)
"""


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.capacity = k
        self.queue = [None] * k
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.tail - self.head < self.capacity:
            self.head -= 1
            self.queue[self.head] = value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.tail - self.head < self.capacity:
            self.queue[self.tail] = value
            self.tail += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.tail - self.head > 0:
            self.head += 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.tail - self.head > 0:
            self.tail -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.tail - self.head > 0:
            return self.queue[self.head]
        else:
            return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.tail - self.head > 0:
            return self.queue[self.tail - 1]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.tail - self.head == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.tail - self.head == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(3)
# print(True)
# print(obj.insertFront(1))
# print(obj.insertLast(2))
# print(obj.insertFront(3))
# print(obj.insertFront(4))
# print(obj.getRear())
# print(obj.isFull())
# print(obj.deleteLast())
# print(obj.insertFront(4))
# print(obj.getFront())

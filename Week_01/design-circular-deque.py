#!/usr/bin/env python
"""
基于双端链表 实现的 双端队列 时间复杂度 增删 O(1),查询 O(n);空间复杂度 O(1)
"""
class deq():
    def __init__(self, value):
        self.va = value
        self.prior = self
        self.next = self

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.head = deq(-1)
        self.tail = deq(-1)
        self.head.next = self.tail
        self.head.prior = self.tail
        self.tail.prior = self.head
        self.tail.next = self.head
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        """
        Adds an value at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size < self.capacity:
            item = deq(value)
            item.next = self.head.next
            item.prior = self.head
            self.head.next.prior = item
            self.head.next = item
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value):
        """
        Adds an value at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size < self.capacity:
            item = deq(value)
            item.prior = self.tail.prior
            item.next = self.tail
            self.tail.prior.next = item
            self.tail.prior = item
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self):
        """
        Deletes an value from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size > 0:
            self.head.next = self.head.next.next
            self.head.next.prior = self.head
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self):
        """
        Deletes an value from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size > 0:
            self.tail.prior = self.tail.prior.prior
            self.tail.prior.next = self.tail
            self.size -= 1
            return True
        else:
            return False

    def getFront(self):
        """
        Get the front value from the deque.
        :rtype: int
        """
        if self.size > 0:
            return self.head.next.va
        else:
            return -1

    def getRear(self):
        """
        Get the last value from the deque.
        :rtype: int
        """
        if self.size > 0:
            return self.tail.prior.va
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.capacity


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

# -*- coding: utf-8 -*-
"""Implementation of queue"""


class Queue:
    """Queue implementation using a list"""

    def __init__(self) -> None:
        """Constructor of queue

        :rtype: None
        """
        self.items: list = []

    def is_empty(self) -> bool:
        """Method Check if queue is empty

        :rtype: bool
        """
        return self.items == []

    def enqueue(self, item: list) -> None:
        """Method Add item to queue

        :param item: item to add
        :rtype: None
        """
        self.items.insert(0, item)

    def dequeue(self) -> list:
        """Method Remove item from queue

        :rtype: list
        """
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.pop(0)

    def size(self) -> int:
        """Method Return size of queue

        :rtype: int
        """
        return len(self.items)
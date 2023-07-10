# -*- coding: utf-8 -*-
"""Implementation of queue"""


class Queue:
    """Queue implementation using a list"""

    def __init__(self) -> None:
        """Initialize"""
        self.items = []

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return self.items == []

    def enqueue(self, item) -> None:
        """Add item to queue"""
        self.items.insert(0, item)

    def dequeue(self) -> list:
        """Remove item from queue"""
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.items.pop(0)

    def size(self) -> int:
        """Return size of queue"""
        return len(self.items)
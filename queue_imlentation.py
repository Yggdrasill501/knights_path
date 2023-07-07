# -*- coding: utf-8 -*-
"""Implementation of queue"""


class Queue:
    """Queue implementation using a list"""

    def __init__(self) -> None:
        """Initialize"""
        self.items = []

    def is_empty(self) -> object:
        """Check if queue is empty"""
        return self.items == []

    def enqueue(self, item) -> None:
        """Add item to queue"""
        self.items.insert(0, item)

    def dequeue(self) -> object:
        """Remove item from queue"""
        return self.items.pop()

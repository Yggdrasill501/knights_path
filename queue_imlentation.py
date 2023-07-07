# -*- coding: utf-8 -*-
"""Implementation of queue"""


class Queue:
    """Queue implementation using a list"""

    def __init__(self):
        """Initialize"""
        self.items = []

    def is_empty(self):
        """Check if queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Add item to queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """Remove item from queue"""
        return self.items.pop()

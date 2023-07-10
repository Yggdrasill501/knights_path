# -*- coding: utf-8 -*-
"""Implementation of breadth first search algorithm for finding the shortest path of knight"""
from queue_imlentation import Queue
from collections import deque

# class BreadthFirstSearch:
#     """Bread first search class"""
#     def __init__(self, grid) -> None:
#         """Initializes"""
#
#         self.grid = grid
#         self.queue = Queue()
#         self.paths = {grid.start: None}
#
#     def find_path(self):
#         """Find path from start to goal"""
#         self.queue.enqueue(self.grid.start)
#
#         while not self.queue.is_empty():
#             current = self.queue.dequeue()
#
#             if current == self.grid.goal:
#                 return self.reconstruct_path(current)
#
#             for next_neighbor in self.grid.get_neighbors(current):
#                 if next_neighbor not in self.paths:
#                     self.paths[next_neighbor] = current
#                     self.queue.enqueue(next_neighbor)
#
#         return None
#
#     def reconstruct_path(self, current) -> tuple:
#         """Reconstruct path from start to goal"""
#         path = []
#
#         while current is not None:
#             path.append(current)
#             current = self.paths[current]
#
#         path.reverse()
#         return path, len(path) - 1


class BFS:
    """Bread first search class"""
    def __init__(self, chessboard):
        """Initializes"""
        self.chessboard = chessboard
        self.directions = [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1)
        ]

    def find_shortest_path(self, start_row, start_col, end_row, end_col):
        """Find shortest path from start to goal"""
        size = self.chessboard.get_size()

        if not self.chessboard.is_valid_move(start_row, start_col) or not self.chessboard.is_valid_move(end_row, end_col):
            raise ValueError("Invalid start or end position.")

        queue = deque([(start_row, start_col)])
        self.chessboard.set_cell(start_row, start_col, 0)

        while queue:
            current_row, current_col = queue.popleft()

            if current_row == end_row and current_col == end_col:
                return self.chessboard.get_cell(current_row, current_col)

            for direction in self.directions:
                next_row = current_row + direction[0]
                next_col = current_col + direction[1]

                if self.chessboard.is_valid_move(next_row, next_col):
                    queue.append((next_row, next_col))
                    self.chessboard.set_cell(next_row, next_col, self.chessboard.get_cell(current_row, current_col) + 1)

        return -1


class Chessboard:
    """Chessboard class"""
    def __init__(self, size):
        """Initializes"""
        self.size = size
        self.board = [[-1 for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row, col):
        """Check if move is valid"""
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == -1

    def get_cell(self, row, col):
        """Get cell value"""
        return self.board[row][col]

    def set_cell(self, row, col, value):
        """Set cell value"""
        self.board[row][col] = value

    def get_size(self):
        """Get size of chessboard"""
        return self.size


# Usage example
# size = 8  # Size of the chessboard
# board = Chessboard(size)
# bfs = BFS(board)
#
# start_row = 0
# start_col = 0
# end_row = 7
# end_col = 7
#
# shortest_path = bfs.find_shortest_path(start_row, start_col, end_row, end_col)
#
# if shortest_path != -1:
#     print(f"Shortest path from ({start_row},{start_col}) to ({end_row},{end_col}): {shortest_path}")
# else:
#     print("No valid path found.")

# Path: queue_imlentation.py

# -*- coding: utf-8 -*-
"""Implementation of a-star heuristics for finding the shortest path of knight"""
from queue import PriorityQueue


class AStar:
    """A-star heuristics class"""
    def __init__(self, chessboard) -> None:
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

    def heuristic(self, row, col, end_row, end_col) -> int:
        # Implementing the Manhattan distance heuristic
        return abs(row - end_row) + abs(col - end_col)

    def find_shortest_path(self, start_row, start_col, end_row, end_col) -> int:
        if not self.chessboard.is_valid_move(start_row, start_col) or not self.chessboard.is_valid_move(end_row, end_col):
            raise ValueError("Invalid start or end position.")

        size = self.chessboard.get_size()
        queue = PriorityQueue()
        queue.put((0, (start_row, start_col)))
        self.chessboard.set_cell(start_row, start_col, 0)

        while not queue.empty():
            _, (current_row, current_col) = queue.get()

            if current_row == end_row and current_col == end_col:
                return self.chessboard.get_cell(current_row, current_col)

            for direction in self.directions:
                next_row = current_row + direction[0]
                next_col = current_col + direction[1]

                if self.chessboard.is_valid_move(next_row, next_col):
                    new_cost = self.chessboard.get_cell(current_row, current_col) + 1
                    if self.chessboard.get_cell(next_row, next_col) == -1 or new_cost < self.chessboard.get_cell(next_row, next_col):
                        self.chessboard.set_cell(next_row, next_col, new_cost)
                        priority = new_cost + self.heuristic(next_row, next_col, end_row, end_col)
                        queue.put((priority, (next_row, next_col)))

        return -1

# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""
from knights_path.chessboard import Chessboard
from knights_path.exeptions import InvalidMove
from knights_path.component_system import log_function_call
from collections import deque
import heapq
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class ShortestPathKnight(Chessboard):
    """Class for the shortest path of knight"""

    def __int__(self, file) -> None:
        """Constructor of ShortestPathKnight

        :param file: file with chessboard
        :rtype: None
        """
        Chessboard.__init__(self, file=file)
        self.knight_moves: list = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]
        self.size: int = len(self.chessboard)

    @log_function_call
    def breath_first_search(self) -> str:
        """Method for breath first search

        :return: number of steps to reach end position
        :rtype: str
        """
        queue = deque([self.start])
        self.chessboard[self.start[0]][self.start[1]] = 0

        while queue:
            row, col = queue.popleft()

            if (row, col) == self.end:
                return self.chessboard[row][col]

            for d_row, d_col in self.knight_moves:
                new_row, new_col = row + d_row, col + d_col

                if self._is_valid_move(new_row, new_col):
                    queue.append((new_row, new_col))
                    self.chessboard[new_row][new_col] = self.chessboard[row][col] + 1
                    queue.append((new_row, new_col))
        else:
            LOGGER.error("No path found")
            sys.exit(1)

    @log_function_call
    def a_star(self) -> str:
        """Method for a star search

        :return: number of steps to reach end position
        :rtype: str
        """
        priority_queue:list = []
        heapq.heappush(priority_queue, (0 + self.heuristic(self.start, self.end), 0,self.start)))

        cost = {self.start: 0}

        while priority_queue:
            _, cost, (row, col) = heapq.heappop(priority_queue)

            if (row, col) == self.end:
                return cost

            for d_row, d_col in self.knight_moves:
                new_row, new_col = row + d_row, col + d_col

                if self.is_valid_move(row=new_row, col=new_col):
                    new_cost = cost + 1

                    if new_cost < cost.get((new_row, new_col), float('inf')):
                        cost[(new_row, new_col)] = new_cost
                        f_cost = new_cost + self.heuristic((new_row, new_col),self.end)
                        heapq.heappush(priority_queue, (f_cost, new_cost, (new_row, new_col)))

    def _is_valid_move(self, row: int, col: int) -> bool:
        """Helper method that check's if the move is valid

        :param row: row of chessboard
        :param col: column of chessboard
        :return: True if move is valid
        :return: False if move is not valid
        :rtype: bool
        """
        try:
            return 0 <= row < self.size and 0 <= col < self.size

        except InvalidMove:
            LOGGER.error("Invalid move")
            sys.exit(1)

    def heuristics(self, start, end) -> int:
        """ Method for heuristics of manhattan distance between two points

        :return: manhattan distance
        :rtype: int
        """
        try:
            return abs(start[0] - end[0]) + abs(start[1] - end[1])

        except InvalidMove:
            LOGGER.error("Invalid move")
            sys.exit(1)

# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""
from breath_first_search.chessboard import Chessboard
from breath_first_search.exeptions import InvalidMove
from breath_first_search.component_system import log_function_call
from collections import deque
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class ShortestPathKnight(Chessboard):
    """Class for the shortest path of knight."""

    def __init__(self, file) -> None:
        """Constructor of ShortestPathKnight.

        :param file: file with chessboard
        :rtype: None
        """
        Chessboard.__init__(self, file=file)
        self.knight_moves: list = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]
        self.size: int = len(self.chessboard)

    @log_function_call
    def breath_first_search(self) -> str:
        """Method for breath first search.

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

    def _is_valid_move(self, row: int, col: int) -> bool:
        """Helper method that check's if the move is valid.

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

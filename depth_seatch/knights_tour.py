# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""
import logging

logging.basicConfig(level=logging.INFO)
MODULE_LOGGER = logging.getLogger(__name__)


class KnightsTour:
    """Class for depth search of playground."""

    def __init__(self,
                 board_size: int) -> None:
        """Constructor.

        :param board_size: int, size of the chessboard
        :rtype None:
        """
        self.chessboard_size = board_size
        self.board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
        self.moves_row = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_colum = [1, 2, 2, 1, -1, -2, -2, -1]

    def _is_valid_move(self, row: int, colum: int):
        """Private method that says if the move is valid.

        :param row: int, row of the chessboard
        :param colum: int, colum of the chessboard
        :returns True: if the move is valid
        :returns False: if the move is not valid
        :rtype bool:
        """
        if 0 <= row < self.chessboard_size and 0 <= colum < self.chessboard_size and self.board[row][colum] == -1:
            MODULE_LOGGER.info("Move is valid")
            return True
        else:
            MODULE_LOGGER.info("No valid move")
            return False

    def warnsdorffs_count(self, row, colum):
        """Method with implementation of Warnsdorff's rule.

        :param row: int, row of the chessboard
        :param colum: int, colum of the chessboard
        :return count: int, count of valid moves
        :rtype int:
        """
        count = 0
        for i in range(self.chessboard_size):
            new_row, new_colum = row + self.moves_row[i], colum + self.moves_colum[i]
            if self._is_valid_move(new_row, new_colum):
                count += 1
        return count

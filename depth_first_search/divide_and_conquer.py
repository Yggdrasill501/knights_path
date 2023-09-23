# -*- coding: utf-8 -*-
"""File for integration of console user interface."""
import logging
import sys

logging.basicConfig(level=logging.INFO)
MODULE_LOGGER = logging.getLogger(__name__)


class KnightsTour:
    """Class for depth search of playground using divide and conquer."""
    def __init__(self,
                 size: int) -> None:
        """Constructor.

        :param size: int, size of the chessboard
        :rtype None:
        """
        self.chessboard_size = size
        self.chessboard = [[-1 for _ in range(self.chessboard_size)] for _ in range(self.chessboard_size)]
        self.moves_row = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_column = [1, 2, 2, 1, -1, -2, -2, -1]

    def _is_valid_move(self,
                       row: int,
                       column: int) -> bool:
        """Private method that says if the move is valid.

        :param row: int, row of the chessboard
        :param column: int, colum of the chessboard
        :returns True: if the move is valid
        :returns False: if the move is not valid
        :rtype bool:
        """
        return 0 <= row < self.chessboard_size and 0 <= column < self.chessboard_size and self.chessboard[row][column] == -1

    def _solve_quarter(self, start_row: int,
                       start_column: int,
                       move_count: int = 0) -> None:
        """Private method that solves quarter of the chessboard.

        :param start_row: int, row of the chessboard
        :param start_column: int, column of the chessboard
        :param move_count: int, number of the move
        :rtype None:
        """
        for i in range(self.chessboard_size // 2):
            for j in range(self.chessboard_size // 2):
                self.chessboard[start_row + i][start_column + j] = move_count
                move_count += 1

    def _stitch_quarters(self) -> None:

        for i in range(self.chessboard_size // 2):
            for j in range(self.chessboard_size // 2):
                self.chessboard[i][j + self.chessboard_size // 2] = self.chessboard[i][j] + (self.chessboard_size ** 2) // 4
                self.chessboard[i + self.chessboard_size // 2][j] = self.chessboard[i][j] + 2 * (self.chessboard_size ** 2) // 4
                self.chessboard[i + self.chessboard_size // 2][j + self.chessboard_size // 2] = self.chessboard[i][j] + 3 * (self.chessboard_size ** 2) // 4

    def find_tour(self) -> None:
        """Method that finds path of the knight.

        :rtype None:
        """
        self._solve_quarter(0, 0)
        self._stitch_quarters()

    def print_tour(self) -> None:
        """Method that prints chessboard.

        :rtype None:
        """
        for i in range(self.chessboard_size):
            for j in range(self.chessboard_size):
                print(f"{self.chessboard[i][j]:4d} ", end='')
            print()

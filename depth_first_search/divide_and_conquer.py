# -*- coding: utf-8 -*-
"""File for integration of console user interface."""
import logging
import sys

logging.basicConfig(level=logging.INFO)
MODULE_LOGGER = logging.getLogger(__name__)


class ConquerorsTour:
    """Class for depth search of playground using divide and conquer."""
    def __init__(self,
                 board_size: int) -> None:
        """Constructor.

        :param board_size: int, size of the chessboard
        :rtype None:
        """
        self.chessboard_size = board_size
        self.chessboard = [[-1 for _ in range(board_size)] for _ in range(board_size)]
        self.moves_row = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_column = [1, 2, 2, 1, -1, -2, -2, -1]

    def _is_valid_move(self, row, column) -> bool:
        return 0 <= row < self.chessboard_size and 0 <= column < self.chessboard_size and self.chessboard[row][column] == -1

    def _solve_quarter(self, start_row, start_column, move_count=0) -> None:
        for i in range(self.chessboard_size // 2):
            for j in range(self.chessboard_size // 2):
                self.chessboard[start_row + i][start_column + j] = move_count
                move_count += 1

    def _stitch_quarters(self) -> None:
        # This is a basic setup, and it assumes the 4 quarters are identical.
        # Advanced implementations can define custom paths to stitch the quarters.
        for i in range(self.chessboard_size // 2):
            for j in range(self.chessboard_size // 2):
                self.chessboard[i][j + self.chessboard_size // 2] = self.chessboard[i][j] + (self.chessboard_size ** 2) // 4
                self.chessboard[i + self.chessboard_size // 2][j] = self.chessboard[i][j] + 2 * (self.chessboard_size ** 2) // 4
                self.chessboard[i + self.chessboard_size // 2][j + self.chessboard_size // 2] = self.chessboard[i][j] + 3 * (self.chessboard_size ** 2) // 4

    def find_tour(self) -> None:
        self._solve_quarter(0, 0)
        self._stitch_quarters()

    def print_tour(self) -> None:
        for i in range(self.chessboard_size):
            for j in range(self.chessboard_size):
                print(f"{self.chessboard[i][j]:4d} ", end='')
            print()


if __name__ == "__main__":
    board_size = 8  # Ensure it's even
    ct = ConquerorsTour(board_size)
    ct.find_tour()
    ct.print_tour()

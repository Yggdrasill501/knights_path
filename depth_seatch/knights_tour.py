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
        self.chessboard = [[-1 for _ in range(board_size)] for _ in range(board_size)]
        self.moves_row = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_colum = [1, 2, 2, 1, -1, -2, -2, -1]

    def find_path(self,
                  start_row: int = 0,
                  start_colum: int = 0):
        """Method that finds path of the knight.

        :param start_row: int
        :param start_colum:
        """
        self.chessboard[start_row][start_colum] = 0
        if not self._depth_first_search(start_row, start_colum, 1):
            MODULE_LOGGER.info("Solution does not exist")
        else:
            self._print_path()

    def _is_valid_move(self,
                       row: int,
                       colum: int) -> bool:
        """Private method that says if the move is valid.

        :param row: int, row of the chessboard
        :param colum: int, colum of the chessboard
        :returns True: if the move is valid
        :returns False: if the move is not valid
        :rtype bool:
        """
        if 0 <= row < self.chessboard_size and 0 <= colum < self.chessboard_size and self.chessboard[row][colum] == -1:
            MODULE_LOGGER.info("Move is valid")
            return True
        else:
            MODULE_LOGGER.info("No valid move")
            return False

    def _warnsdorffs_count(self,
                           row: int,
                           colum: int) -> int:
        """Private method with implementation of Warnsdorff's rule.

        :param row: int, row of the chessboard
        :param colum: int, colum of the chessboard
        :return count: int, count of valid moves
        :rtype int:
        """
        count: int = 0
        for i in range(self.chessboard_size):
            new_row, new_colum = row + self.moves_row[i], colum + self.moves_colum[i]
            if self._is_valid_move(new_row, new_colum):
                count += 1
        return count

    def _depth_first_search(self,
                            row: int,
                            colum: int,
                            move_count: int) -> bool:
        """Private method for implementation of depth first search algorithm.
        Sort possible moves by Warnsdorff's rule (smallest number of onward moves)

        :param row: int, row of the chessboard
        :param colum: int, colum of the chessboard
        :param move_count: int, count of moves of knight on the chessboard
        :returns True: if knight moves are possible on the chessboard
        :returns False: if knight moves are not possible on the chessboard
        :rtype bool:
        """
        if move_count == self.chessboard_size * self.chessboard_size:
            return True

        possible_knight_moves: list = []

        for i in range(self.chessboard_size):
            new_row, new_colum = row + self.moves_row[i], colum + self.moves_colum[i]

            if self._is_valid_move(new_row, new_colum):
                possible_knight_moves.append((new_row, new_colum, self._warnsdorffs_count(new_row, new_colum)))

        possible_knight_moves.sort(key=lambda t: t[2])

        for new_row, new_col, _ in possible_knight_moves:
            self.chessboard[new_row][new_col] = move_count
            if self._depth_first_search(new_row, new_col, move_count + 1):
                return True
            self.chessboard[new_row][new_col] = -1

        return False

    def _print_path(self) -> None:
        """Private method that prints path of the knight

        :rtype None:
        """
        for i in range(self.chessboard_size):
            for j in range(self.chessboard_size):
                print(f"{self.chessboard[i][j]:2d} ", end='')
            print()

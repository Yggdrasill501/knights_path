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
        self.moves_column = [1, 2, 2, 1, -1, -2, -2, -1]
        self.count_of_possible_moves = len(self.moves_row)

    def find_path(self,
                  start_row: int = 0,
                  start_column: int = 0):
        """Method that finds path of the knight.

        :param start_row: int
        :param start_column:
        """
        self.chessboard[start_row][start_column] = 0

        if not self._depth_first_search(start_row, start_column, 1):
            MODULE_LOGGER.info("Solution does not exist")
        else:
            MODULE_LOGGER.info("finding path*")
            self._print_path()

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
        if 0 <= row < self.chessboard_size and 0 <= column < self.chessboard_size and self.chessboard[row][column] == -1:
            MODULE_LOGGER.info("Move is valid")
            return True
        else:
            MODULE_LOGGER.info("No valid move")
            return False

    def _warnsdorffs_count(self,
                           row: int,
                           column: int) -> int:
        """Private method with implementation of Warnsdorff's rule.

        :param row: int, row of the chessboard
        :param column: int, colum of the chessboard
        :return count: int, count of valid moves
        :rtype int:
        """
        count: int = 0
        for i in range(self.count_of_possible_moves):
            new_row, new_column = row + self.moves_row[i], column + self.moves_column[i]
            if self._is_valid_move(new_row, new_column):
                count += 1
        return count

    def _depth_first_search(self,
                            row: int,
                            column: int,
                            move_count: int) -> bool:
        """Private method for implementation of depth first search algorithm.
        Sort possible moves by Warnsdorff's rule (smallest number of onward moves)

        :param row: int, row of the chessboard
        :param column: int, colum of the chessboard
        :param move_count: int, count of moves of knight on the chessboard
        :returns True: if knight moves are possible on the chessboard
        :returns False: if knight moves are not possible on the chessboard
        :rtype bool:
        """
        if move_count == self.chessboard_size * self.chessboard_size:
            return True

        possible_knight_moves: list = []

        for i in range(self.count_of_possible_moves):
            new_row, new_column = row + self.moves_row[i], column + self.moves_column[i]

            if self._is_valid_move(new_row, new_column):
                possible_knight_moves.append((new_row, new_column, self._warnsdorffs_count(new_row, new_column)))

        possible_knight_moves.sort(key=lambda t: t[2])

        for new_row, new_column, _ in possible_knight_moves:
            self.chessboard[new_row][new_column] = move_count
            if self._depth_first_search(new_row, new_column, move_count + 1):
                return True
            self.chessboard[new_row][new_column] = -1

        return False

    def _print_path(self) -> None:
        """Private method that prints path of the knight

        :rtype None:
        """
        for i in range(self.chessboard_size):
            for j in range(self.chessboard_size):
                print(f"{self.chessboard[i][j]:2d} ", end='')
            print()

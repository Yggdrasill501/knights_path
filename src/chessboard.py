# -*- coding: utf-8 -*-
"""Chessboard implementation file"""


class Chessboard:
    """Chessboard class"""
    def __init__(self, size: int) -> None:
        """Constructor of chessboard

        :param size: size of chessboard
        :rtype: None
        """
        self.size: int = size
        self.board: list = [[-1 for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row: int, col: int) -> bool:
        """Method Check if move is valid

        :param row: row int of chessboard
        :param col: column int of chessboard
        :return True: if move is valid
        :return False: if move is invalid
        :rtype: bool
        """
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == -1

    def get_cell(self, row: int, col: int) -> int:
        """Method Get cell value

        :param row: row int of chessboard
        :param col: column int of chessboard
        :return: value of cell
        :rtype: int
        """
        return self.board[row][col]

    def set_cell(self, row, col, value) -> None:
        """Method Set cell value

        :param row: row int of chessboard
        :param col: column int of chessboard
        :param value: value to set
        :rtype: None
        """
        self.board[row][col] = value

    def get_size(self) -> int:
        """Method Get size of chessboard

        :return size: size of chessboard
        :rtype: int
        """
        return self.size

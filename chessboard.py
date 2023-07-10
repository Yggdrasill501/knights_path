# -*- coding: utf-8 -*-
"""Settings for playground"""


class Chessboard:
    """Chessboard class"""
    def __init__(self, size) -> None:
        """Initializes"""
        self.size = size
        self.board = [[-1 for _ in range(size)] for _ in range(size)]

    def is_valid_move(self, row, col) -> bool:
        """Check if move is valid"""
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == -1

    def get_cell(self, row, col) -> int:
        """Get cell value"""
        return self.board[row][col]

    def set_cell(self, row, col, value) -> None:
        """Set cell value"""
        self.board[row][col] = value

    def get_size(self) -> int:
        """Get size of chessboard"""
        return self.size

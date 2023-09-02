# -*- coding: utf-8 -*-
"""File reads chessboard file"""
import logging
import sys

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


class ChessBoard:
    """Read gird from file and find neighbors of a position."""

    def __init__(self, file) -> None:
        """Constructor of chessboard

        :param file: file with chessboard
        :rtype: None
        """
        try:
            with open(file, 'r') as file:
                self.grid = [list(line.strip()) for line in file]

            self.start, self.goal = None, None
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j] == 'S':
                        self.start = (i, j)

                    elif self.grid[i][j] == 'E':
                        self.goal = (i, j)

            if self.start is None or self.goal is None:
                logging.error("Start or goal not found in the grid.")
                sys.exit(1)

        except FileNotFoundError:
            logging.error("file doesnt exist or is empty")
            sys.exit(1)

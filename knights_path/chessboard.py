# -*- coding: utf-8 -*-
"""File reads chessboard file."""
import logging
import sys
from knights_path.exeptions import InvalidChessboard

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


class Chessboard:
    """Read gird from file and find neighbors of a position."""

    def __init__(self, file) -> None:
        """Constructor of chessboard.

        :param file: file with chessboard
        :rtype: None
        """
        try:
            with open(file, 'r') as file:
                self.chessboard = [list(line.strip()) for line in file]

            self.start, self.end = None, None
            for i in range(len(self.chessboard)):
                for j in range(len(self.chessboard[0])):
                    if self.chessboard[i][j] == 'S':
                        self.start = (i, j)

                    elif self.chessboard[i][j] == 'E':
                        self.end = (i, j)

            if self.start is None or self.end is None:
                logging.error("Start or goal not found in the grid.")
                sys.exit(1)

        except FileNotFoundError:
            logging.error("file doesnt exist or is empty")
            sys.exit(1)

        except InvalidChessboard:
            logging.error("Invalid chessboard")
            sys.exit(1)

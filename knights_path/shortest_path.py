# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""
import sys
from random import randint, choice
import logging
from collections import deque
import pathlib
# from my_queue.queue import Queue


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class ShortestPathKnight:
    """Class for the shortest path of knight"""

    def __int__(self) -> None:
        """Constructor of ShortestPathKnight
        :rtype: None
        """
        self.knight_moves: list = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]
        self.start_position = None
        self.end_position = None
        self.chessboard: list = []

    def chessboard_from_file(self, file: pathlib.Path) -> list:
        """Method that load chess board from file

        :exception FileNotFound:

        :param file: pathlib.Path file, with chess board size, obstacles and start and end
        :return list: self._chessboard
        :retype list:
        """
        try:
            with open(file, 'r') as file:
               self.chessboard = [list(line.strip()) for line in file]

            for i in range(len(self.chessboard)):
                for j in range(len(self.chessboard[0])):
                    if self.chessboard[i][j] == 'S':
                        self.start_position = (i, j)

                    elif self.chessboard[i][j] == 'E':
                        self.end_position = (i, j)

            return self.chessboard

        except FileNotFoundError:
            logging.error("file doesnt exist or is empty")
            sys.exit(1)

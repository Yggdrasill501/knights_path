# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""
import queue
from random import randint, choice
import logging
import threading

from my_queue.queue import Queue


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


class ShortestPathKnight:
    """Class for the shortest path of knight"""

    def __int__(self, end_position: tuple,
                chessboard_size: int = 3,
                obstacles: bool = False,
                start_position: tuple = (0, 0),
                random_positions: bool = False) -> None:
        """Constructor of ShortestPathKnight

        :param end_position: end position of knight
        :param chessboard_size: size of chessboard
        :param obstacles: if True, obstacles will be generated
        :param obstacles: if False, obstacles will not be generated
        :param start_position: start position of knight
        :param random_positions: if True, start position will be generated randomly
        :rtype: None
        """

        self._chessboard_size: int = chessboard_size
        self._obstacles: bool = obstacles
        self._start_position: tuple = start_position
        self._end_position: tuple = end_position
        self._random: bool = random_positions

        self._chessboard = []

    def _chessboard_generator(self) -> list:
        """Method Generate chessboard

        :return chessboard: generated chessboard
        :rtype: list
        """
        self._chessboard = [[0 for _ in range(self._chessboard_size)] for _ in range(self._chessboard_size)]
        logging.info("Chessboard: %s", self._chessboard)

        return self._chessboard

    def _obstacles(self) -> list:
        """Method that add random obstacles to the chessboard

        :return list: chessboard with obstacles
        :rtype: list
        """

        if self._obstacles:
            for i in range(self._chessboard_size//3):
                zero_coords = [(row, col) for row, line in enumerate(self._chessboard) for col, value in enumerate(line) if value == 0]

                if zero_coords:
                    row, col = choice(zero_coords)
                    self._chessboard[row][col] = 1
        logging.info("Chessboard with obstacles: %s", self._chessboard)

        return self._chessboard

    def _placement(self) -> list:
        """Method that add knight to the chessboard

        :return list: chessboard with knight
        :rtype: list
        """
        if self._random:
            self._start_position = (randint(0, self._chessboard_size-1), randint(0, self._chessboard_size-1))
            # TODO: append random start position to the chessboard
            self._end_position = (randint(0, self._chessboard_size-1), randint(0, self._chessboard_size-1))
            # TODO: append random end position to the chessboard

        else:
            # TODO: append random start position to the chessboard
            # TODO: append random end position to the chessboard
            pass

        logging.info("Chessboard with knight: %s", self._chessboard)

        return self._chessboard

    def bfs(self) -> list:
        """Method that implement BFS algorythm

        :return: shortest path
        :rtype: list
        """
        # Todo: implement BFS
        Queue.dequeue()

        logging.info("Shortest path: %s", self._chessboard)
        return self._chessboard
        pass

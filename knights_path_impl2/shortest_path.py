# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""
from random import randint

class ShortestPathKnight:
    """Class for the shortest path of knight"""

    def __int__(self,end_position: tuple,
                chessboard_size: int = 3,
                obstacles: bool = False,
                start_position: tuple = (0,0),
                random_positions : bool = False) -> None:
        """Constructor

        :param end_position: end position of knight
        :param chessboard_size: size of chessboard
        :param obstacles: if True, obstacles will be generated
        :param obstacles: if false, obstacles will not be generated
        :param start_position: start position of knight
        :param random_positions: if True, start position will be generated randomly
        :rtype: None
        """

        self._chessboard_size: int = chessboard_size
        self._obstacles: bool = obstacles
        self._start_position: tuple = start_position
        self._end_position: tuple = end_position

    def _generate_chessboard(self) -> list:
        """Method Generate chessboard

        :return chessboard: generated chessboard
        :rtype: list
        """
        chessboard = [[_ for i in range(self._chessboard_size)] for _ in range(self._chessboard_size)]

        return chessboard

    def _positions(self) -> list:
        """Method for positions of knight

        :return list: list of positions
        :rtype: list
        """

    def _obstacles(self) -> list:
        """Method that add random obstacles to the chessboard

        :return list: chessboard with obstacles
        :rtype: list
        """

        chessboard_with_obstacles = self._generate_chessboard()

        return chessboard_with_obstacles

if __name__ == '__main__':
    pass
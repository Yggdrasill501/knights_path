# -*- coding: utf-8 -*-
"""Algorythm for shortest path of knight."""


class ShortestPath:
    """Class for the shortest path of knight"""

    def __int__(self, chessboard_size: int = 3, obstacles: bool = False, ) -> None:
        """Constructor

        :param chessboard_size: size of chessboard
        :param obstacles: if True, obstacles will be generated
        :param obstacles: if false, obstacles will not be generated
        :rtype: None
        """

        self.chessboard_size: int = chessboard_size
        self.obstacles: bool = obstacles

    def generate_chessboard(self) -> list:
        """Method Generate chessboard

        :return chessboard: generated chessboard
        :rtype: list
        """
        chessboard = [[_ for i in range(self.chessboard_size)] for _ in range(self.chessboard_size)]

        return chessboard

if __name__ == '__main__':
    pass
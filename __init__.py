# -*- coding: utf-8 -*-
from algorythm import KnightsPath
from point import Point
from settings import*


if __name__ == '__main__':
    knightspath = KnightsPath(playground=chess_board_size)
    knightspath.run()
    
    start = Point(0, 0)
    end = Point(7,7)
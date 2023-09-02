# -*- coding: utf-8 -*-
import logging
from knights_path.shortest_path import ShortestPathKnight


logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


def user_interface(chessboard_file):
    """Function for user interface"""
    print("Welcome to the shortest path of knight.")
    print("Please enter file with chessboard, start position as S and end position as E.")
    print("Minimal chessboard size is 3x3")


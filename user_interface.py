# -*- coding: utf-8 -*-
"""File with user interface"""
import logging
from knights_path.shortest_path import ShortestPathKnight
import time

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


def user_interface(chessboard_file):
    """Function for user interface"""
    print("Welcome to the shortest path of knight.")
    print("Please enter file with chessboard, start position as S and end position as E, or edit existing one.")
    print("Minimal chessboard size is 3x3")
    shortest_path = ShortestPathKnight(chessboard_file)
    time.sleep(1)
    print(f"Minimal number of steps to reach end position is {shortest_path.breath_first_search()}")

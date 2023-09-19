# -*- coding: utf-8 -*-
"""File with user interface."""
import logging
from breath_first_search.shortest_path import ShortestPathKnight

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


def user_interface(chessboard_file):
    """Function for user interface"""
    print("Welcome to the shortest path of knight.")
    print("Please enter file with chessboard, start position as S and end position as E, or edit existing one.")
    print("Minimal chessboard size is 3x3")

    x = input("Enter file name: ")

    shortest_path = ShortestPathKnight(chessboard_file)



    print(f"Minimal number of steps to reach end position is {shortest_path.breath_first_search()}")

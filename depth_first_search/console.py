# -*- coding: utf-8 -*-
"""File for integration of console user interface."""
import depth_first_search.recursive
import depth_first_search.divide_and_conquer

import logging
import sys

logging.basicConfig(level=logging.ERROR)
MODULE_LOGGER = logging.getLogger(__name__)


def user_interface():
    """Method that starts user interface."""
    try:
        board_size = int(input("Enter the chessboard size: "))

        option = str(input("Chose if you want to use recursive (type R) or divide and conquer (type Q)"))

        if option == 'R' or option == 'r':
            search = depth_first_search.recursive.KnightsTour(board_size)
            search.find_path()

        elif option == 'Q' or option == 'q':
            search = depth_first_search.devide_and_conquer.KnightsTour(board_size)
            search.find_path()

    except ValueError as e:
        MODULE_LOGGER.error(f"You entered wrong value into chessboard size, program raised {e}")
        sys.exit(1)

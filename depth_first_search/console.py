# -*- coding: utf-8 -*-
"""File for integration of console user interface."""
from depth_first_search.knights_tour import KnightsTour

import logging
import sys

logging.basicConfig(level=logging.ERROR)
MODULE_LOGGER = logging.getLogger(__name__)


def user_interface():
    """Method that starts user interface."""
    try:
        board_size = int(input("Enter the board size: "))
        search = KnightsTour(board_size)

        print(f"Path of knight is {search.find_path()}")

    except ValueError as e:
        MODULE_LOGGER.error(f"You entered wrong value into board size, program raised {e}")
        sys.exit(1)

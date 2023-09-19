# -*- coding: utf-8 -*-
"""File for integration of console user interface."""

import logging
import sys

logging.basicConfig(level=logging.ERROR)
MODULE_LOGGER = logging.getLogger(__name__)


class ConsoleUi:
    """Class for integration with user via console."""
    def __init__(self) -> None:
        """Constructor.

        :rtype None:
        """

    def user_interface(self):
        print("Hello user, you started knights tour program")
        try:
            board_size = int(input("Enter the board size: "))

        except ValueError as e:
            MODULE_LOGGER.error(f"You entered wrong value into board size, program raised {e}")
            sys.exit(1)

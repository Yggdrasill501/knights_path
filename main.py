# -*- coding: utf-8 -*-
"""Main file, runs whole code."""
from breath_first_search.user_interface import user_interface
from depth_seatch.console_ui import ConsoleUi

import sys
import logging

logging.basicConfig(level=logging.ERROR)
MODULE_LOGGER = logging.getLogger(__name__)


if __name__ == "__main__":
    print("Hello user, you started Knights Path program")
    print("Please enter what kind of Knights Path problem you want to solve")

    console_runner: bool = True

    while console_runner:
        try:
            option = str(input("If you want to solve shortest path enter B or b, \n"
                               "If you want solve every visit of knight enter D or d. "))

            if option == 'B' or option == 'b':
                user_interface()

                console_runner = False

            elif option == 'D' or option == 'd':
                ConsoleUi.user_interface()

                console_runner = False

            else:
                print("Please enter correct option")

        except ValueError as e:
            MODULE_LOGGER.error(f"You entered wrong value, program raised {e}")
            print("Please enter correct option")

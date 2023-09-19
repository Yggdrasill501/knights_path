# -*- coding: utf-8 -*-
"""Main file, runs whole code."""
import logging
import breath_first_search.console
import depth_first_search.console

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
                breath_first_search.console.user_interface()
                console_runner = False

            elif option == 'D' or option == 'd':
                depth_first_search.console.user_interface()
                console_runner = False

            else:
                print("Please enter correct option")

        except ValueError as e:
            MODULE_LOGGER.error(f"You entered wrong value, program raised {e}")
            print("Please enter correct option")

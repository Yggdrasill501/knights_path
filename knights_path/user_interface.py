# -*- coding: utf-8 -*-
import logging
# import argparse

logging.basicConfig(level=logging.ERROR)


class UserInterface:
    """Class for interaction with user"""

    def __int__(self) -> None:
        """Constructor

        :rtype: None
        """

    def user_interface(self):
        """Method that interact with user"""
        print("Hello, this is the program that will show you the shortest path of knight")
        try:
            chessboard_size = int(input("Enter size of chessboard: "))
        except ValueError:
            logging.error("Invalid input type")
            return -1

        try:
            game_mode = str(input("if you want to knight to go trough all fields enter 'y', if you want to knight to go to specific field enter 'n': "))
        except ValueError:
            logging.error("Invalid input type")
            return -1

        if game_mode == 'y':
            knight_row = 0
            knight_col = 0

        else:
            try:
                random_position = str(input("Do you want to random position of knight? (y/n): "))
            except ValueError:
                logging.error("Invalid input type")
                return -1

            if random_position == 'n':
                knight_row = int(input("Enter row of knight: "))
                knight_col = int(input("Enter column of knight: "))

        try:
            obstacles = str(input("Do you want to add random obstacles? (y/n): "))
        except ValueError:
            logging.error("Invalid input type")
            return -1

        return chessboard_size, game_mode, knight_row, knight_col, obstacles

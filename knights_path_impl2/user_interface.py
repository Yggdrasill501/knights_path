# -*- coding: utf-8 -*-
import logging
import argparse

logging.basicConfig(level=logging.INFO)


class UserInterface:
    """Class for interaction with user"""

    def __int__(self) -> None:
        """Constructor

        :rtype: None
        """

    def talk(self):
        """

        """
        print("Hello, this is the program that will show you the shortest path of knight")
        chessboard_size = int(input("Enter size of chessboard: "))

        game_mode = str(input("if you want to knight to go trough all fields enter 'y', if you want to knight to go to specific field enter 'n': "))
        if game_mode == 'y':
            knight_row = 0
            knight_col = 0

        else:
            random_position = str(input("Do you want to random position of knight? (y/n): "))
            if random_position == 'n':
                knight_row = int(input("Enter row of knight: "))
                knight_col = int(input("Enter column of knight: "))

        obstacles = str(input("Do you want to add random obstacles? (y/n): "))


# -*- coding: utf-8 -*-
import logging
import threading
import argparse
from abc import abstractmethod

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


class UserInterface:
    """Class for interaction with user"""
    def __init__(self) -> None:
        """Constructor of UserInterface

        :rtype: None
        """
        self._chessboard_size: int = 3

    def _user_interface(self):
        """Method that interact with user"""
        print("Hello, this is the program that will show you the shortest path of knight")
        try:
            self.chessboard_size = int(input("Enter size of chessboard: "))
            logging.info("Chessboard size: %s", self.chessboard_size)

        except ValueError:
            logging.error("Invalid input type")
            return -1

        try:
            game_mode = str(input("if you want to knight to go trough all fields enter 'y', if you want to knight to go to specific field enter 'n': "))
            logging.info("Game mode: %s", game_mode)

        except ValueError:
            logging.error("Invalid input type")
            return -1

        if game_mode == 'y':
            knight_row = 0
            knight_col = 0

        else:
            try:
                random_position = str(input("Do you want to random position of knight? (y/n): "))
                logging.info("Random position: %s", random_position)

            except ValueError:
                logging.error("Invalid input type")
                return -1

            if random_position == 'n':
                try:
                    knight_row = int(input("Enter row of knight: "))
                    logging.info("Knight row: %s", knight_row)

                    knight_col = int(input("Enter column of knight: "))
                    logging.info("Knight column: %s", knight_col)

                except ValueError:
                    logging.error("Invalid input type")
                    return -1

        try:
            obstacles = str(input("Do you want to add random obstacles? (y/n): "))
            logging.info("Obstacles: %s", obstacles)

        except ValueError:
            logging.error("Invalid input type")
            return -1

        try:
            return self.chessboard_size, game_mode, knight_row, knight_col, obstacles

        except UnboundLocalError:
            logging.error("Return error")
            return -1

    @abstractmethod
    def run(self):
        """Method that run program"""
        self._user_interface()
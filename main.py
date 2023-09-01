# -*- coding: utf-8 -*-
"""Main file"""
import logging

from user_interface import UserInterface

LOGGER = logging.getLogger(__name__)


if __name__ == '__main__':
    ui = UserInterface()
    ui.run()
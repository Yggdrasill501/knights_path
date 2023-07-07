# -*- coding: utf-8 -*-
"""File to generate playground grid"""
from abc import abstractmethod
from random import randint

class GeneratePlayground:
    """Class that generates playground with or without obstacles"""
    def __init__(self) -> None:
        """Initialize"""
        self.playground_size : int
        self.playground_grid: list

        self.playground_size = 4
        self.playground_grid = [
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
            ['_', '_', '_', '_'],
        ]

    def user_input(self) -> int:
        """Method for user input"""
        size: int

        print("You need to enter size of playground that you wanna you for knight,")
        print("If you doesnt enter the size will 4x4 ")
        print("The size of the playground is square so you enter just one number ")
        size = int(input("Enter the size of the playground: " ))
        if size is None or size < 4 or int(size) != size:
            self.playground_size = self.playground_size
        else:
            self.playground_size = size
        return self.playground_size

    def create_grid(self) -> list:
        """Create playground grid"""
        x: list = []
        y: list = []

        if self.playground_size <= 4:
            return self.playground_grid
        else:
            self.playground_grid.clear()
            x.append(self.playground_size * '_')
            y.append(self.playground_size * x)
            self.playground_grid.append(y)
            return self.playground_grid

    def random_obstacles(self):
        """Generate random obstacles on the playground grid"""

        obstacle: str = '|'
        for i in range(len(self.playground_grid)):
            for y in range(len(self.playground_grid[i])):
                number_of_obstacles = int(self.playground_size // 4)


    @abstractmethod
    def run(self) -> None:
        """Runs Generate playground Class"""
        obstacles: str

        self.user_input()
        self.create_grid()
        obstacles = str(input("If you wanna generate obstacles in way type: Y, if not just press enter." ))
        if obstacles == 'Y':
            self.random_obstacles()
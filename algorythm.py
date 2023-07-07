# -*- coding: utf-8 -*-
"""File"""
from abc import abstractclassmethod, abstractproperty, abstractstaticmethod, abstractmethod
from collections import deque
from functools import lru_cache
from point import Point
                
class Figure:
    def __init__(self) -> None:
        self.dx : list
        self.dy : list


class KnightsPath:
    """ """
    def __init__(self, playground : list) -> None:
        """Initiate the class"""
        
        self.playground = playground
        self.dx = [2, 2, -2, -2, 1, 1, -1, -1]
        self.dy = [1, -1, 1, -1, 2, -2, 2, -2]    
    
    @property
    def valid_path(self, x : int, y : int) -> bool:
        return 0 <= x < self.playground and 0 <= y < self.playground

    @lru_cache(maxsize=None)
    def find_path(self, start : tuple, end : tuple) -> int:
        """Method for finding path of on Playground"""
        queue = queue()
        queue.append((start, 0))
        visited = [[False for _ in range(self.playground)] for _ in range(self.playground)]
        visited[start.x][start.y] = True
        
        while queue:
            point, distance = queue.popleft()
            if point.x == end.x and point.y == end.y:
                return distance
            
            for i in range(8):
                x = point.x + self.dx[i]
                y = point.y + self.dy[i]
                if self.valid_pathp(x=x, y=y) and not visited[x][y]:
                    queue.append((Point(x, y), distance + 1))
                    visited[x][y] = True
                    
        print("Path is not found")
        return -1 # if no path exists

        @abstractmethod
        def run(self) -> None:
            """Method to run the class"""
            self.find_path
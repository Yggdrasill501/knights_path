# -*- coding: utf-8 -*-
"""Main file"""
from src.a_star_heuristics import AStar
from src.breadth_first_search import BreadthFirstSearch
from src.generate_playground import GeneratePlayground
from analyse.analysis import Analysis


if __name__ == '__main__':
    astar = AStar
    bfs = BreadthFirstSearch
    generate = GeneratePlayground
    analise = Analysis

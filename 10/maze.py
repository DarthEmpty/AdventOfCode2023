from enum import Enum, auto
from typing import List, Tuple, Dict
from  colorama import init as cr_init, Fore, Style
from dataclasses import dataclass

import numpy as np

COORDS = Tuple[np.ndarray]

cr_init()


CARDINALS = {
    "north": (-1, 0),
    "east" : (0, 1),
    "south": (1, 0),
    "west" : (0, -1)
}


class Maze:
    PIPE_DIRECTIONS = {
        "|": (CARDINALS["north"], CARDINALS["south"]),
        "L": (CARDINALS["north"], CARDINALS["east"]),
        "J": (CARDINALS["north"], CARDINALS["west"]),
        "F": (CARDINALS["south"], CARDINALS["east"]),
        "7": (CARDINALS["south"], CARDINALS["west"]),
        "-": (CARDINALS["east"], CARDINALS["west"]),
    }
    
    def __init__(self, grid: List[List[str]]) -> "Maze":
        self._grid = np.array(grid)
        self._visited = np.zeros(self._grid.shape, dtype=np.int64)
        
        self.start = np.where(self._grid == "S")
        
        # Can replace S symbol given the input
        self._grid[self.start] = "J"
    
    def __str__(self) -> str:
        unvisited_char = "`"
        color_in = np.vectorize(lambda s: Fore.GREEN + s if s != unvisited_char else Style.RESET_ALL + s)
        revealed = color_in(np.where(self._visited, self._grid, unvisited_char))
        
        return "\n".join(["".join(row) for row in revealed])
    
    def visit(self, coords: COORDS):
        self._visited[coords] = 1
    
    def has_been_visited(self, coords: COORDS) -> bool:
        return self._visited[coords]
    
    def get_neighbours(self, coords:COORDS) -> List[COORDS]:        
        return [
            (coords[0] + direction[0], coords[1] + direction[1])
            for direction in Maze.PIPE_DIRECTIONS[self._grid[coords][0]]
        ]

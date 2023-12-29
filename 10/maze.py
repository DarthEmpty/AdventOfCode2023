from enum import Enum, auto
from typing import List, Tuple, Dict, Iterable
from  colorama import init as cr_init, Fore, Style
from dataclasses import dataclass

import numpy as np

COORD = Tuple[int]

cr_init()


def to_coord(array: np.ndarray) -> COORD:
        return (int(array[0]), int(array[1]))


# String enum (in the absence of the functionality in 3.10)
class TileType:
    NORTHSOUTH = "|"
    NORTHEAST = "L"
    NORTHWEST = "J"
    SOUTHEAST = "F"
    SOUTHWEST = "7"
    EASTWEST = "-"
    START = "S"
    GROUND = "."


class Cardinal(Enum):
    NORTH = auto()
    EAST  = auto()
    SOUTH = auto()
    WEST  = auto()


class Maze:
    VALID_TILES_IN_DIRECTION = {
        Cardinal.NORTH: (
            TileType.NORTHSOUTH,
            TileType.SOUTHEAST,
            TileType.SOUTHWEST
        ),
        Cardinal.EAST: (
            TileType.EASTWEST,
            TileType.NORTHWEST,
            TileType.SOUTHWEST
        ),
        Cardinal.SOUTH: (
            TileType.NORTHSOUTH,
            TileType.NORTHEAST,
            TileType.NORTHWEST
        ),
        Cardinal.WEST: (
            TileType.EASTWEST,
            TileType.NORTHEAST,
            TileType.SOUTHEAST
        )
    }
    
    def __init__(self, grid: List[List[str]]) -> "Maze":
        self.grid = np.array(grid)
        self.visited = np.zeros(self.grid.shape, dtype=np.int64)
        self.start = to_coord(np.where(self.grid == TileType.START))
        
    
    def __str__(self) -> str:
        
        color_in = np.vectorize(lambda s: Fore.GREEN + s if s != "`" else Style.RESET_ALL + s)
        revealed = color_in(np.where(self.visited, self.grid, "`"))
        
        return "\n".join(["".join(row) for row in revealed])

    def is_in_bounds(self, tile: COORD) -> bool:
        return tile[0] >= 0 and tile[0] < np.size(self.grid, 0) \
            and tile[1] >= 0 and tile[1] < np.size(self.grid, 1)
    
    def visit(self, tile: COORD):
        self.visited[tile] = 1

    def get_adjacent_tiles(self, tile: COORD) -> Dict[Cardinal, COORD]:
        row, col = tile
        adjacent_tiles = {
            Cardinal.NORTH: (row - 1, col),
            Cardinal.EAST : (row, col + 1),
            Cardinal.SOUTH: (row + 1, col),
            Cardinal.WEST : (row, col - 1),
        }
        
        for adj in adjacent_tiles:
            if not self.is_in_bounds(adjacent_tiles[adj]):
                adjacent_tiles.pop(adj)
        
        return adjacent_tiles
    
    def get_children(self, parent_tile: COORD) -> List[COORD]:
        adjacent_tiles = self.get_adjacent_tiles(parent_tile)
        children = []
        
        for cardinal in adjacent_tiles:
            tile = adjacent_tiles[cardinal]
            if self.grid[tile] in Maze.VALID_TILES_IN_DIRECTION[cardinal]:
                children.append(tile)
        
        return children


# @dataclass
# class Tile:
#     coord: COORD
#     parent: "Tile" = None
#     children: List["Tile"] = []
    
#     def 
        
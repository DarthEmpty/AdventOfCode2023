from enum import Enum, auto
from typing import List, Tuple, Dict

import numpy as np

COORD = Tuple[int]


def to_coord(array: np.ndarray) -> COORD:
        return (int(array[0]), int(array[1]))


# String enum (in the abcense of the functionality in 3.10)
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

    def is_valid(self, tile: COORD) -> bool:
        return tile[0] >= 0 and tile[0] < np.size(self.grid, 0) \
            and tile[1] >= 0 and tile[1] < np.size(self.grid, 1)

    def get_adjacent_tiles(self, tile: COORD) -> Dict[Cardinal, COORD]:
        row, col = tile
        adjacent_tiles = {
            Cardinal.NORTH: (row - 1, col),
            Cardinal.EAST : (row, col + 1),
            Cardinal.SOUTH: (row + 1, col),
            Cardinal.WEST : (row, col - 1),
        }
        
        for adj in adjacent_tiles:
            if not self.is_valid(adjacent_tiles[adj]):
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
        
import numpy as np

from maze import Maze, TileType, to_coord

FILENAME = "10/input.txt"


def part_1(maze: Maze) -> int:
    start = to_coord(np.where(maze.grid == TileType.START))
    children = []
    explored = set()
    current_tile = start
    steps = 0
    
    # TODO: Figure out why len(explored) and steps are so different
    while current_tile not in explored:
        children.extend([
            (child, steps + 1)
            for child in maze.get_children(current_tile)
            if child not in explored
        ])
        
        explored.add(current_tile)
        current_tile, steps = children.pop(0)
    
    return steps


def part_2(maze: np.ndarray) -> int:
    return 0


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    maze = Maze([[char for char in line] for line in contents])
    print(part_1(maze))
    print(part_2(maze))


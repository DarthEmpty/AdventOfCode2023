import numpy as np

from maze import Maze

FILENAME = "10/input.txt"


def part_1(maze: Maze) -> int:
    children = []
    current_tile = maze.start
    steps = 0
    
    # TODO: Recreate Maze file to consider shape of current pipe
    while not maze.visited[current_tile]:
        children.extend([
            (child, steps + 1)
            for child in maze.get_children(current_tile)
            if not maze.visited[child]
        ])
        
        maze.visit(current_tile)
        current_tile, steps = children.pop(0)
    
    print(maze)
    
    return steps


def part_2(maze: np.ndarray) -> int:
    return 0


if __name__ == "__main__":    
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    maze = Maze([[char for char in line] for line in contents])
    print(part_1(maze))
    print(part_2(maze))


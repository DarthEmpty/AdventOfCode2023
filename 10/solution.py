import numpy as np

from maze import Maze

FILENAME = "10/input.txt"


def part_1(maze: Maze) -> int:
    current = maze.start
    steps = 0
    to_visit = []
    
    while not maze.has_been_visited(current):
        maze.visit(current)
        to_visit.extend(
            (steps + 1, neighbour)
            for neighbour in maze.get_neighbours(current)
            if not maze.has_been_visited(neighbour)
        )        
        
        steps, current = to_visit.pop(0)
    
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


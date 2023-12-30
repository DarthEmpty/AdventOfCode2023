import numpy as np

from maze import Maze, CARDINALS

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
    
    return steps


def part_2(maze: Maze) -> int:
    inside = False
    pipes_seen = []
    pipes_enclosed = 0
    
    for coord, pipe in np.ndenumerate(maze._grid):        
        if inside and not maze.has_been_visited(coord):
            pipes_enclosed += 1
        
        elif maze.has_been_visited(coord):
            pipes_seen.extend(Maze.PIPE_DIRECTIONS[pipe])
            
            norths = pipes_seen.count(CARDINALS["north"])
            souths = pipes_seen.count(CARDINALS["south"])
            
            # Crossing 2 pipes that both point north or both point south
            # means that we've towed the border of the loop
            # and haven't entered it
            if norths > 1 or souths > 1:
                pipes_seen.clear()
            
            # If we cross a north-pointing pipe and a south pointing pipe
            # in the same row, we have crossed the border of the loop.
            elif norths == 1 and souths == 1:
                inside = not inside
                pipes_seen.clear()

    return pipes_enclosed


if __name__ == "__main__":    
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    maze = Maze([[char for char in line] for line in contents])
    print(part_1(maze))
    print(part_2(maze))
    print(maze)


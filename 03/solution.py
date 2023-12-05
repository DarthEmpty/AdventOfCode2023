from typing import List, Tuple
import numpy as np
import re
import string

FILENAME = "03/input.txt"


def is_valid(scematic_grid: np.ndarray, index: Tuple[int]) -> bool:
    row, col = index
    
    return row >= 0 and col >= 0 \
        and row < scematic_grid.shape[0] and col < scematic_grid.shape[1]


def capture_number_from_digit(
    scematic_grid: np.ndarray,
    index: Tuple[int]
) -> Tuple[int, List[Tuple[int]]]:
    
    l_bound = r_bound = index[1]
    digit_coords = set([index])
    
    # look left
    while is_valid(scematic_grid, (index[0], l_bound - 1)) and scematic_grid[index[0], l_bound - 1] in string.digits:
        l_bound -= 1
        digit_coords.add((index[0], l_bound))
    
    # look right
    while is_valid(scematic_grid, (index[0], r_bound)) and scematic_grid[index[0], r_bound] in string.digits:
        r_bound += 1
        digit_coords.add((index[0], r_bound))
    
    digits = scematic_grid[index[0], l_bound : r_bound]
    
    return int("".join(d for d in digits)), digit_coords


def get_adjacent_numbers(scematic_grid: np.ndarray, index: Tuple[int]):
    row, col = index
    
    adjacent_coords = [
        (row-1, col-1), (row-1, col), (row-1, col+1),
        (row  , col-1),               (row  , col+1),
        (row+1, col-1), (row+1, col), (row+1, col+1)
    ]
    
    adjacent_numbers = []
    checked_coords = set()
    for coord in adjacent_coords:
        if coord in checked_coords or scematic_grid[coord] not in string.digits:
            continue
        
        number, digit_coords = capture_number_from_digit(scematic_grid, coord)
        adjacent_numbers.append(number)
        checked_coords.update(digit_coords)
    
    return adjacent_numbers


def part_1(contents: np.ndarray) -> int:
    engine_parts = []
    
    for i, char in np.ndenumerate(contents):
        if char != "." and char not in string.digits:
            engine_parts.extend(get_adjacent_numbers(contents, i))
    
    return sum(engine_parts)


def part_2(contents: List[str]) -> int:
    ratios = []
    
    for i, char in np.ndenumerate(contents):
        if char != "*":
            continue
        
        adjacents = get_adjacent_numbers(contents, i)
        if len(adjacents) != 2:
            continue
        
        ratios.append(adjacents[0] * adjacents[1])
            
    return sum(ratios)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    contents = [list(line) for line in contents]
    schematic_grid = np.array(contents)
    
    print(part_1(schematic_grid))
    print(part_2(schematic_grid))


from typing import List
from math import prod
import re

FILENAME = "02/input.txt"
MAXIMUM = {"red": 12, "green": 13, "blue": 14}


def is_possible(game: List[str]) -> bool:
    for result in game:
        quantity, colour = result.split(" ")
        if int(quantity) > MAXIMUM[colour]:
            return False
        
    return True


def get_power(game: List[str]) -> int:
    minimum = {"red": 0, "green": 0, "blue": 0}
    
    for result in game:
        quantity, colour = result.split(" ")
        quantity = int(quantity)
        if minimum[colour] < quantity:
            minimum[colour] = quantity
    
    return prod(minimum.values())


def part_1(contents: List[str]) -> int:
    return sum(i for i, game in enumerate(contents, 1) if is_possible(game))


def part_2(contents: List[str]) -> int:
    return sum(get_power(game) for game in contents)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    drawn_cubes = [re.findall(r"\d+ red|\d+ blue|\d+ green", game) for game in contents]
    
    print(part_1(drawn_cubes))
    print(part_2(drawn_cubes))


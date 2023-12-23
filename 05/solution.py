from typing import List, Tuple, Dict

import re

FILENAME = "05/input.txt"

# Source range: Dest range
MAP = Dict[range, int]


def to_map(map: List[Tuple[int, int, int]]) -> MAP:
    return {
        range(source, source + length): dest
        for dest, source, length in sorted(map, key=lambda x: x[1])
    }


def interpret(contents: List[str]) -> Tuple[List[int], List[MAP]]:
    seeds = [int(match) for match in re.findall(r"\d+", contents.pop(0))]
    triplets = []

    for line in contents:
        if not line:
            triplets.append(list())
        
        # Dest Start, Source Start, Range Length
        elif (numbers := re.match(r"(\d+) (\d+) (\d+)", line)):
            triplets[-1].append(tuple(int(num) for num in numbers.groups()))
    
    return seeds, [to_map(triplet) for triplet in triplets]


def apply_map_to_source(map: MAP, source: int):
    for source_range in map:
        if source in source_range:
            difference = source - source_range.start
            return map[source_range] + difference
        
    return source


def part_1(seeds: List[int], maps: List[MAP]) -> int:
    smallest = None
    
    for seed in seeds:
        location = seed
        for map in maps:
            location = apply_map_to_source(map, location)
        
        if not smallest or location < smallest:
            smallest = location
    
    return smallest


def part_2(seeds: List[int], maps: List[MAP]) -> int:           
    return 0


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    seeds, maps = interpret(contents)
    
    print(part_1(seeds, maps))
    print(part_2(seeds, maps))


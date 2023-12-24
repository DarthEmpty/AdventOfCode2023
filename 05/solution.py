from typing import List, Tuple, Dict
from itertools import chain

import re

FILENAME = "05/input.txt"

TRIPLET = Tuple[int, int, int]

# Source range: Dest
MAP = Dict[range, int]


def str_to_seeds(seed_string: str) -> List[int]:
    return [int(match) for match in re.findall(r"\d+", seed_string)]


def str_to_seed_ranges(seed_string: str) -> List[range]:
    matches = str_to_seeds(seed_string)
    return [
        range(matches[i], matches[i] + matches[i + 1])
        for i in range(0, len(matches), 2)
    ]


def triplets_to_map(map: List[TRIPLET]) -> MAP:
    return {
        range(source, source + length): dest
        for dest, source, length in sorted(map, key=lambda x: x[1])
    }


def extract_triplets(triplet_list: List[str]) -> List[TRIPLET]:
    triplets = []

    for line in triplet_list:
        if not line:
            triplets.append(list())
        
        # Dest Start, Source Start, Range Length
        elif (numbers := re.match(r"(\d+) (\d+) (\d+)", line)):
            triplets[-1].append(tuple(int(num) for num in numbers.groups()))
            
    return triplets


def interpret(
        contents: List[str],
        seed_ranges=False
    ) -> Tuple[List[int] | List[range], List[MAP]]:
    
    seed_string = contents.pop(0)
    
    return (
        str_to_seed_ranges(seed_string) if seed_ranges
        else str_to_seeds(seed_string),
        
        [triplets_to_map(triplet) for triplet in extract_triplets(contents)]
    )


def containing_range(map: MAP, source: int) -> range | None:
    for key_range in map:
        if source in key_range:
            return key_range
    
    return None


def transform_source(map: MAP, source: int, key_range: range):
    return map[key_range] + source - key_range.start


def apply_map_to_source(map: MAP, source: int) -> int:
    if not (key_range := containing_range(map, source)):
        return source
    
    return transform_source(map, source, key_range)


def apply_map_to_source_range(map: MAP, source: range) -> List[range]:
    res = []
    start_key_range = containing_range(map, source.start)
    
    # We take 1 away from the stop point to find the range
    # that contains the last number in the source
    stop_key_range = containing_range(map, source.stop - 1)
    
    if not start_key_range and not stop_key_range:        
        res.append(source)
    
    elif start_key_range == stop_key_range:
        res.append(range(
            transform_source(map, source.start, start_key_range),
            transform_source(map, source.stop, stop_key_range)
        ))
    
    else:
        separation_point = start_key_range.stop \
            if start_key_range \
            else stop_key_range.start
        
        difference = separation_point - source.start
        res.extend(apply_map_to_source_range(map, source[:difference]))
        res.extend(apply_map_to_source_range(map, source[difference:]))
        
    return res
        


def part_1(seeds: List[int], maps: List[MAP]) -> int:
    smallest = None
    
    for seed in seeds:
        location = seed
        for map in maps:
            location = apply_map_to_source(map, location)
        
        if not smallest or location < smallest:
            smallest = location
    
    return smallest


def part_2(seed_ranges: List[range], maps: List[MAP]) -> int:
    all_locations = []
    
    for seed_range in seed_ranges:
        locations = [seed_range]
        for map in maps:
            new_locations = [
                apply_map_to_source_range(map, location_range)
                for location_range in locations
            ]
            
            locations.clear()
            
            for location_list in new_locations:
                locations.extend(location_list)

        all_locations.extend(locations)
    
    return sorted(all_locations, key=lambda r: r.start)[0].start


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    print(part_1(*interpret(contents.copy())))
    print(part_2(*interpret(contents, seed_ranges=True)))


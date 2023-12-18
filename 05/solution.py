from typing import List, Tuple, Collection
from sortedcontainers import SortedDict

import re

FILENAME = "05/input.txt"

# Source Start : (Dest Start, Range Length)
ALMANAC_MAP = SortedDict[int, Tuple[int, int]]


def to_maps(contents: List[str]) -> Tuple[List[int], List[ALMANAC_MAP]]:
    seeds = [int(match) for match in re.findall(r"\d+", contents.pop(0))]
    maps = []
        
    for line in contents:
        if not line:
            maps.append(SortedDict())
        
        # Dest Start, Source Start, Range Length
        elif (numbers := re.match(r"(\d+) (\d+) (\d+)", line)):
            dest, source, length = numbers.groups()
            maps[-1][int(source)] = (int(dest), int(length))
            
    return seeds, maps


def seed_range_generator(seeds: List[int]) -> Collection[Tuple[int, int]]:
    for i in range(0, len(seeds), 2):
        yield seeds[i], seeds[i] + seeds[i + 1]
        

def closest_key_in_map(map: ALMANAC_MAP, source: int) -> int:
    index = map.bisect(source) - 1
    
    # There's no key that satisfies the number.
    if index == -1:
        return -1
    
    return map.keys()[index]


def relevant_keys_in_map(map: ALMANAC_MAP, source: Tuple[int, int]) -> List[int]:
    keys = [key for key in map if source[0] <= key and key <= source[1]]
    
    closest_key = closest_key_in_map(map, source[0])
    if closest_key != -1:
        keys.append(closest_key)
    
    return keys


def apply_map(map: ALMANAC_MAP, source: int) -> int:
    closest_key = closest_key_in_map(map, source)
    
    if closest_key == -1:
        return source
    
    dest, length = map[closest_key]
    
    # The key most likely to have a mapping for source doesn't have one.
    if source not in range(closest_key, closest_key + length):
        return source
    
    return dest + source - closest_key


def apply_map_to_range(map: ALMANAC_MAP, source: Tuple[int, int]) -> List[Tuple[int, int]]:
    results = []
    
    for key in relevant_keys_in_map(map, source):
        dest, length = map[key]
        range_end = key + length
        
        if key <= source[0]:
            results.append((source[0], range_end))
            source = (range_end + 1, source[1])
            
        elif source[1] <= range_end:
            results.append(())
        
        else:
            
        
        if source[1] > range_end:
            results.extend(apply_map_to_range(map, (range_end + 1, source[1])))
            source = (source[0], range_end)
        
        if key <= source[0] and source[1] <= range_end: 
            results.append((
                dest + source[0] - key,
                dest + source[1] - key
            ))
    
    results.append(source)
        
    return results
        


def part_1(seeds: List[int], maps: List[ALMANAC_MAP]) -> int:
    min_location = -1
    
    for seed in seeds:
        location = seed
        
        for map in maps:
            location = apply_map(map, location)
        
        min_location = location if min_location < 0 \
                        or location < min_location else min_location
    
    return min_location


def part_2(seeds: List[int], maps: List[ALMANAC_MAP]) -> int:
    seed_ranges = [pair for pair in seed_range_generator(seeds)]

    for map in maps:
        outputs = []
        
        for seed_range in seed_ranges:
            outputs.extend(apply_map_to_range(map, seed_range))
        
        seed_ranges = outputs
            
    return min(location[0] for location in seed_ranges)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    seeds, maps = to_maps(contents)
    
    print(part_1(seeds, maps))
    print(part_2(seeds, maps))


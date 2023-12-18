from typing import List, Tuple
from math import prod, sqrt, ceil, floor
import re

FILENAME = "06/input.txt"


def to_int_list(contents: str) -> List[int]:
    return [int(res) for res in re.findall(r"\d+", contents)]


def to_joined_int(contents: str) -> int:
    return int("".join(re.findall(r"\d+", contents)))


def find_quadratic_roots(a: float, b: float, c: float) -> Tuple[float, float]:
    discriminant = b**2 - 4*a*c
    root_1 = (-b + sqrt(discriminant)) / (2*a)
    root_2 = (-b - sqrt(discriminant)) / (2*a)
    
    return root_1, root_2


def part_1(contents: List[str]) -> int:
    max_times = to_int_list(contents[0])
    record_dists = to_int_list(contents[1])
    
    # Distance travelled is a function of time spent holding the button (dD/dt).
    # "Time holding" equals the speed that the boat travels (t = v)
    # "Distance travelled" equals speed multiplied by time spent moving (D=vt_m)
    # "Time Moving" equals the total time minus time spent holding (t_m = T - t)
    # ...Therefore: t_m = T - v, then D = v(T - v)    
    
    # All points between the 2 "roots" where the record distance (d_r) meets D = v(T - v)
    # beat the record, and should be included in the result
    
    root_pairs = [
        find_quadratic_roots(-1, T, -d_r)
        for T, d_r in zip(max_times, record_dists)
    ]                    
    
    return prod(
        int(root_2) - int(root_1)
        for root_1, root_2 in root_pairs
    )


def part_2(contents: List[str]) -> int:
    max_time = to_joined_int(contents[0])
    record_dist = to_joined_int(contents[1])
    
    root_1, root_2 = find_quadratic_roots(-1, max_time, -record_dist)
    
    return int(root_2) - int(root_1)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    print(part_1(contents))
    print(part_2(contents))

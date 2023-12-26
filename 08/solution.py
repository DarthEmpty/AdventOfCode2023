from typing import List, Tuple, Dict, Callable, Generator, Any
from math import lcm
import re

FILENAME = "08/input.txt"
NETWORK = Dict[str, Tuple[str, str]]


def interpret(contents: List[str]) -> Tuple[List[int], NETWORK]:
    directions = [
        0 if direction == "L" else 1
        for direction in contents[0]
    ]
    
    nodes = [re.findall(r"\w{3}", line) for line in contents[2:]]
    network = {
        node: (left, right)
        for node, left, right in nodes
    }
    
    return directions, network


def path_gen(
    start: str,
    directions: List[int],
    network: NETWORK
) -> Generator[Tuple[int, str], Any, None]:
    
    current_node = start
    steps = 0
    
    while True:
        direction = directions[steps % len(directions)]
        current_node = network[current_node][direction]
        steps += 1
        yield steps, current_node
        

def steps_travelled(
    start: str,
    end_condition: Callable,
    directions: List[int],
    network: NETWORK
) -> int:
    
    current_node = start
    path_nodes = path_gen(current_node, directions, network)
    steps = 0
    
    while not end_condition(current_node):
        steps, current_node = next(path_nodes)
    
    return steps
    

def part_1(directions: List[int], network: NETWORK) -> int:    
    return steps_travelled(
        "AAA", lambda node: node == "ZZZ",
        directions, network
    )


def part_2(directions: str, network: NETWORK) -> int:
    start_nodes = [node for node in network if node.endswith("A")]
    steps_per_path = [
        steps_travelled(
            start_node, lambda node: node.endswith("Z"),
            directions, network
        ) 
        for start_node in start_nodes
    ]
    
    # After running tests on the data, we know
    # that each path loops back on itself.
    # So, we can find the lowest common multiple of the steps
    # between **A and **Z for each path.
    return lcm(*steps_per_path)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    directions, network = interpret(contents)
    print(part_1(directions, network))
    print(part_2(directions, network))


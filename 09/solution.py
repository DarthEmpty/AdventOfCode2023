from typing import List
import re

FILENAME = "09/input.txt"


def is_zero_sequence(sequence: List[int]) -> bool:
    return len(seq_set := set(sequence)) == 1 and 0 in seq_set


def difference_sequence(sequence):
    return [
        sequence[i + 1] - sequence[i]
        for i in range(len(sequence) - 1)
    ]


def next_number_in(sequence: List[int]) -> int:
    if is_zero_sequence(sequence):
        return 0
    
    return sequence[-1] + next_number_in(difference_sequence(sequence))


def prev_number_in(sequence: List[int]) -> int:
    if is_zero_sequence(sequence):
        return 0
    
    return sequence[0] - prev_number_in(difference_sequence(sequence))


def part_1(sequences: List[List[int]]) -> int:   
    return sum(next_number_in(sequence) for sequence in sequences)


def part_2(sequences: List[List[int]]) -> int:
    return sum(prev_number_in(sequence) for sequence in sequences)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    sequences = [
        [int(res) for res in re.findall(r"-?\d+", line)]
        for line in contents
    ]
    
    print(part_1(sequences))
    print(part_2(sequences))


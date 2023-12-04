from typing import List
import regex as re


FILENAME = "01/input.txt"
DIGIT_MAP = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9"
}


def convert_digits(digit_list: List[str]) -> List[str]:
    # Look up the value of the list element in DIGIT_MAP.
    # If it's not there, then it's already in the right format.
    
    return [
        DIGIT_MAP[digit]
        if digit in DIGIT_MAP else digit
        for digit in digit_list
    ]


def part_1(contents: List[str]) -> int:
    digit_groups = [re.findall(r"\d", line) for line in contents]
    numbers = [int(digits[0] + digits[-1]) for digits in digit_groups]

    return sum(numbers)


def part_2(contents: List[str]) -> int:    
    pattern = "\d|" + "|".join(DIGIT_MAP)
    digit_groups = [re.findall(pattern, line, overlapped=True) for line in contents]
    converted_groups = [convert_digits(group) for group in digit_groups]
    numbers = [int(group[0] + group[-1]) for group in converted_groups]

    return sum(numbers)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    print(part_1(contents))
    print(part_2(contents))


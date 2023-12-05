from typing import List
from sortedcontainers import SortedList
import re

FILENAME = "04/input.txt"


def part_1(contents: List[str]) -> int:
    total_points = 0
    
    for card in contents:
        winning_nos = set(card[:10])
        possessed_nos = set(card[10:])
        if (power := len(winning_nos.intersection(possessed_nos))) > 0:
            total_points += 2**(power-1)
    
    return total_points


def part_2(contents: List[str]) -> int:
    # card_collection is a mapping between the card ID and the quantity of said card.
    # i.e. At first, we have 1 copy of all cards
    card_collection = [1 for _ in range(len(contents))]
    
    for i, card in enumerate(contents):
        winning_nos = set(card[:10])
        possessed_nos = set(card[10:])
        quantity_won = len(winning_nos.intersection(possessed_nos))
        
        # Identical cards will always produce the same result
        # so we don't have to evaluate them individually.
        # Cards won would increase by the number copies of the current card that we have.
        for won_id in range(i + quantity_won, i, -1):
            card_collection[won_id] += card_collection[i]
    
    return sum(card_collection)


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    contents = [line.split(":")[1] for line in contents]
    cards = [re.findall(r"\d+", line) for line in contents]
    
    print(part_1(cards))
    print(part_2(cards))


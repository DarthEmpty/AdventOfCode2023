from typing import List

from poker_hand import PokerHand, JokerHand

FILENAME = "07/input.txt"


def part_1(contents: List[str]) -> int:
    hands = [line.split(" ") for line in contents]
    hands = sorted([PokerHand(hand[0], int(hand[1])) for hand in hands])
    
    return sum(
        rank * hand.bid
        for rank, hand in enumerate(hands, start=1)
    )


def part_2(contents: List[str]) -> int:
    hands = [line.split(" ") for line in contents]
    hands = sorted([JokerHand(hand[0], int(hand[1])) for hand in hands])
    
    return sum(
        rank * hand.bid
        for rank, hand in enumerate(hands, start=1)
    )


if __name__ == "__main__":
    with open(FILENAME) as file:
        contents = file.read().splitlines()
    
    print(part_1(contents))
    print(part_2(contents))


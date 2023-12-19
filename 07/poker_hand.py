from enum import IntEnum
from operator import itemgetter


class PokerHand:
    Type = IntEnum("Type", [
        "HIGH_CARD", "ONE_PAIR", "TWO_PAIRS",
        "THREE_OAK", "FULL_HOUSE", "FOUR_OAK",
        "FIVE_OAK"
    ])
    
    Cards = "123456789TJQKA"
    
    def __init__(self, contents: str, bid: int) -> "PokerHand":
        self.contents = contents
        self.bid = bid
        self.type = self.get_type(contents)
        
    def __hash__(self) -> int:
        return hash(self.contents)
    
    def __eq__(self, other: "PokerHand") -> bool:
        return self._compare_to(other) == 0
    
    def __gt__(self, other: "PokerHand") -> bool:
        return self._compare_to(other) == 1
    
    def __ge__(self, other: "PokerHand") -> bool:
        return self._compare_to(other) in (1, 0)
    
    def __lt__(self, other: "PokerHand") -> bool:
        return self._compare_to(other) == -1
    
    def __le__(self, other: "PokerHand") -> bool:
        return self._compare_to(other) in (-1, 0)
    
    @classmethod
    def get_type(cls, contents) -> "Type":
        card_frequency = [
            contents.count(card)
            for card in set(contents)
        ]
        
        if 5 in card_frequency:
            return cls.Type.FIVE_OAK
        
        if 4 in card_frequency:
            return cls.Type.FOUR_OAK
        
        if 3 in card_frequency and 2 in card_frequency:
            return cls.Type.FULL_HOUSE
        
        if 3 in card_frequency:
            return cls.Type.THREE_OAK
        
        if card_frequency.count(2) == 2:
            return cls.Type.TWO_PAIRS
        
        if 2 in card_frequency:
            return cls.Type.ONE_PAIR
        
        return cls.Type.HIGH_CARD
        
    
    def _compare_to(self, other: "PokerHand") -> int:
        if self.type > other.type:
            return 1
        
        if self.type < other.type:
            return -1
        
        # Same type, must compare cards
        for card_1, card_2 in zip(self.contents, other.contents):
            index_1 = self.Cards.index(card_1)
            index_2 = self.Cards.index(card_2)
            
            if index_1 > index_2:
                return 1
            
            if index_1 < index_2:
                return -1
        
        return 0


class JokerHand(PokerHand):
    Cards = "J123456789TQKA"

    @classmethod
    def get_type(cls, contents: str) -> "PokerHand.Type":
        if "J" not in contents or len(set(contents)) == 1:
            return super().get_type(contents)
        
        card_dict = dict(sorted([
            (card, contents.count(card))
            for card in set(contents)
        ], key=itemgetter(1), reverse=True))
                
        card_dict.pop("J")
        highest_freq_card = list(card_dict.keys())[0]
        contents = contents.replace("J", highest_freq_card)
        
        return super().get_type(contents)
            
        
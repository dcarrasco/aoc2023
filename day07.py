"""
AOC Advent of code 2023
Day 07
"""

from dataclasses import dataclass
from aoc import get_data
from collection import Collection


@dataclass
class Hand:
    cards: str = ""

    def cards_dict(self):
        cards_dict = {}
        for c in self.cards:
            if c not in cards_dict:
                cards_dict[c] = 0
            cards_dict[c] += 1
        return cards_dict

    def get_type(self):
        cards_dict = self.cards_dict()
        max_q = max([v for k, v in cards_dict.items()])
        # print(self.cards, cards_dict, max_q, cards_dict.items())
        hand_type = ''
        if len(cards_dict) == 1:
            hand_type = "5 five of a kind"
        elif len(cards_dict) == 2:
            if max_q == 4:
                hand_type = "4 of a kind"
            if max_q == 3:
                hand_type = "full house"
        elif len(cards_dict) == 3:
            if max_q == 3:
                hand_type = "3 of a kind"
            if max_q == 2:
                hand_type = "2 pair"
        elif len(cards_dict) == 4:
            if max_q == 2:
                hand_type = "1 pair"
        elif len(cards_dict) == 5:
            hand_type = "highest"
        return hand_type

    def get_type2(self):
        return Hand(self.replace_jokers()).get_type()

    def type_rank(self):
        return {
            "5 five of a kind": "7",
            "4 of a kind": "6",
            "full house": "5",
            "3 of a kind": "4",
            "2 pair": "3",
            "1 pair": "2",
            "highest": "1"
        }

    def card_rank(self):
        return {
            '2': '01', '3': '02', '4': '03', '5': '04', '6': '05', '7': '06', '8': '07',
            '9': '08', 'T': '09', 'J': '10', 'Q': '11', 'K': '12', 'A': '13'
        }

    def card_rank2(self):
        return {
            '2': '01', '3': '02', '4': '03', '5': '04', '6': '05', '7': '06', '8': '07',
            '9': '08', 'T': '09', 'J': '00', 'Q': '11', 'K': '12', 'A': '13'
        }

    def rank(self):
        return self.type_rank()[self.get_type()] + "".join([self.card_rank()[c] for c in self.cards])

    def rank2(self):
        return self.type_rank()[self.get_type2()] + "".join([self.card_rank2()[c] for c in self.cards])

    def replace_jokers(self):
        cards = self.cards.replace('J', '')

        if cards == '':
            new_cards = 'AAAAA'
        else:
            # print(cards)
            card_dict = {}
            for c in cards:
                if c not in card_dict:
                    card_dict[c] = 0
                card_dict[c] += 1
            # print(card_dict)
            max_repeat = max([v for k, v in card_dict.items()])
            max_card = [(c, self.card_rank2()[c]) for c in card_dict if card_dict[c] == max_repeat]
            max_card = sorted(max_card, key=lambda c: c[1])[-1][0]
            # print(max_repeat, max_card)

            new_cards = self.cards.replace('J', max_card)

        return new_cards


def proc_data(data: Collection) -> 'Collection':
    return data.filter_blanks() \
        .map(lambda lin: {"hand": Hand(lin.split(" ")[0]), "bid": int(lin.split(" ")[1])})


def part1(is_test: bool):
    """
    Primera parte
    """
    data = get_data(test=is_test).process(proc_data)
    print(data)
    # for a in data:
    #     print(a)
    #     print(a["hand"].get_type())
    data.map(lambda g: g["hand"].rank())
    ordered_hands = sorted(data.all(), key=lambda h: h["hand"].rank())
    total = [(hand["bid"], i + 1) for i, hand in enumerate(ordered_hands)]
    print(Collection(total).map(lambda e: e[0] * e[1]).sum())


def part2(is_test: bool):
    """
    Segunda parte
    """
    data = get_data(test=is_test).process(proc_data)
    print(data)
    ordered_hands = sorted(data.all(), key=lambda h: h["hand"].rank2())
    # print(ordered_hands)
    total = [(hand["bid"], i + 1) for i, hand in enumerate(ordered_hands)]
    print(Collection(total).map(lambda e: e[0] * e[1]).sum())


if __name__ == "__main__":
    is_test = True
    print('================================================')
    part1(is_test)
    print('================================================')
    part2(is_test)

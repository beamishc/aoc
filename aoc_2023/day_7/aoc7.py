from icecream import ic
from collections import Counter

cards_dct = {'A': 14, 'K':13, 'Q':12, 'J': 11, 'T': 10, '9': 9, '8': 8,
             '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def day_7_1(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')
        hands = [line.split()[0] for line in lines]
        bets = [line.split()[1] for line in lines]

        lst = []
        for i, hand in enumerate(hands):
            results = Counter(hand).values()
            values = [cards_dct[x] for x in hand]
            if 5 in results:
                lst.append((7, *(values), int(bets[i])))
            elif 4 in results:
                lst.append((6, *(values), int(bets[i])))
            elif 3 in results:
                if 2 in results:
                    lst.append((5, *(values), int(bets[i])))
                else:
                    lst.append((4, *(values), int(bets[i])))
            elif [1,2,2] == sorted(results):
                lst.append((3, *(values), int(bets[i])))
            elif [1,1,1,2] == sorted(results):
                lst.append((2, *(values), int(bets[i])))
            else:
                lst.append((1, *(values), int(bets[i])))
        final = sorted(lst)

    return sum([x[-1]*(i+1) for i, x in enumerate(final)])

ic(day_7_1('day_7/input.txt'))

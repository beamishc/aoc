from icecream import ic

def day_4_1(textfile):
    with open(textfile) as f:
        lines = f.readlines()

        total = 0

        for line in lines:
            w_nums, c_nums = line.split(': ')[1].split(' | ')

            per_card = 0

            for card_num in [int(x) for x in c_nums.split()]:
                if card_num in [int(x) for x in w_nums.split()]:
                    if per_card == 0:
                        per_card = 1
                    else:
                        per_card = per_card *2
            total += per_card
    return total

print(day_4_1('aoc_2023/day_4/input.txt'))

def set_list(s):
    return set([int(x) for x in s.split()])

def day_4_2(textfile):
    with open(textfile) as f:
        lines = f.readlines()

        cards_dct = {}

        for line in lines:
            card_info, content = line.split(': ')
            card_no = int(card_info.split()[1])
            win_nums, card_nums = content.split(' | ')
            wins_on_card = len(set_list(card_nums)).intersection(set_list(win_nums))

            cards_dct[card_no] = {'wins_on_card': wins_on_card, 'copies': 1, 'count': 1}

        for card_no in cards_dct.keys():
            for i in range(1, cards_dct[card_no]['wins_on_card']+1):
                    for copy in range(1, cards_dct[card_no]['copies']+1):
                        cards_dct[card_no+i]['count'] += 1
                        cards_dct[card_no+i]['copies'] += 1

    return sum([cards_dct[card]['count'] for card in cards_dct.keys()])

print(day_4_2('aoc_2023/day_4/input.txt'))

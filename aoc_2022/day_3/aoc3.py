import string
from collections import Counter

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
alphadict = dict(zip(alphabet, range(1,53)))

def day_3_1(input):

    with open(input) as f:
        rucksacks = f.readlines()

    result = 0

    for sack in rucksacks:
        middle = len(sack)//2
        comp1Set = set(Counter(sack[:middle]))
        comp2Set = set(Counter(sack[middle:]))

        for letter in comp1Set.intersection(comp2Set):
            result += alphadict[letter]
    print(result)

day_3_1('day_3/input.txt')


def day_3_2(input):

    with open(input) as f:
        rucksacks = f.readlines()

    result = 0

    groups = {}
    i, j = 0, 1

    for sack in rucksacks:
        i+=1
        groups.setdefault(j, []).append(Counter(sack))
        if i%3 == 0:
            j+=1

    for key in groups.keys():
        guess1, guess2 = [],[]
        for letter in set(groups[key][0]).intersection(set(groups[key][1])):
            if letter != '\n':
                guess1.append(letter)
        for letter in set(groups[key][1]).intersection(set(groups[key][2])):
            if letter != '\n':
                guess2.append(letter)
        for letter in guess1:
            if letter in guess2:
                result += alphadict[letter]
    print(result)

day_3_2('day_3/input.txt')

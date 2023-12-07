# from icecream import ic
from functools import reduce

def day_6_1(textfile):
    with open(textfile) as f:
        lines = [line.split(':')[1].split() for line in f.read().strip().split('\n')]
        lines = {int(k):int(v) for k,v in zip(lines[0], lines[1])}

        total = 1

        for k,v in lines.items():
            current_race = 0
            for i in range(1, k):
                travel_time = k - i
                hold_time = i
                distance = hold_time * travel_time
                if distance > v:
                    current_race += 1
            total = total * current_race
        return total


print(day_6_1('day_6/input.txt'))


def day_6_2(textfile):
    with open(textfile) as f:
        lines = [line.split(':')[1] for line in f.read().strip().split('\n')]
        lines = {int(''.join(lines[0].strip().split())):int(''.join(lines[1].strip().split()))}

        total = 1

        for k,v in lines.items():
            current_race = sum(i * (k - i) > v for i in range(1, k))
            total = total * current_race
        return total

print(day_6_2('day_6/test_1.txt'))


def day_6_1_one_line(textfile):
    with open(textfile) as f:
        lines = [line.split(':')[1].split() for line in f.read().strip().split('\n')]
        lines = {int(k):int(v) for k,v in zip(lines[0], lines[1])}

        return reduce(lambda x, y: x*y, [sum(i * (k - i) > v for i in range(1, k)) for k,v in lines.items()])

print(day_6_1_one_line('day_6/input.txt'))

def day_6_2_one_line(textfile):
    with open(textfile) as f:
        lines = [line.split(':')[1] for line in f.read().strip().split('\n')]
        lines = {int(''.join(lines[0].strip().split())):int(''.join(lines[1].strip().split()))}

        return reduce(lambda x, y: x*y, [sum(i * (k - i) > v for i in range(1, k)) for k,v in lines.items()])

print(day_6_2_one_line('day_6/test_1.txt'))

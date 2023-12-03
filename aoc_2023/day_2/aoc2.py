from icecream import ic

def day_2_1(textfile):
    with open(textfile) as f:
        lines = f.readlines()

    relevant_games = []

    for line in lines:
        max_counts = {'red': 0, 'green': 0, 'blue': 0}
        start, content = line.strip().split(':')
        results = list(content.split('; '))
        for result in results:
            ball_counts = list(result.split(', '))
            for count in ball_counts:
                amount, type = count.strip().split()
                if int(amount) > max_counts[type]:
                    max_counts[type] = int(amount)
        if max_counts['red'] <= 12:
            if max_counts['green'] <= 13:
                if max_counts['blue'] <= 14:
                    relevant_games.append(int(start.split()[1]))

    return sum(relevant_games)

print(day_2_1('aoc_2023/day_2/input.txt'))

def day_2_2(textfile):
    with open(textfile) as f:
        lines = f.readlines()

    total = 0

    for line in lines:
        mins = {'red': 0, 'green': 0, 'blue': 0}
        results = list(line.strip().split(':')[1].split('; '))
        for result in results:
            ball_counts = list(result.split(', '))
            for count in ball_counts:
                amount, type = count.strip().split()
                if int(amount) > mins[type]:
                    mins[type] = int(amount)
        total += mins['red'] * mins['green'] * mins['blue']

    return total

print(day_2_2('aoc_2023/day_2/input.txt'))

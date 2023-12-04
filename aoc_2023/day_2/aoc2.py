from icecream import ic

def day_2_1(textfile):
    with open(textfile) as f:
        lines = f.readlines()

    relevant_games = []

    for line in lines:

        # create a dictionary for each colour
        max_counts = {'red': 0, 'green': 0, 'blue': 0}

        # string manipulation to get game_no and results
        start, content = line.strip().split(':')

        # for loop through results
        for result in list(content.split('; ')):
            ball_counts = list(result.split(', '))

            # for loop through number of balls for each result
            for count in ball_counts:
                amount, type = count.strip().split()

                # check if current result amount is greater than dictionary amount
                if int(amount) > max_counts[type]:
                    # replace if so
                    max_counts[type] = int(amount)

        # nested if statements to check for required minimum number of balls and append if met
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
        # create dictionary for minimum counts of colours
        mins = {'red': 0, 'green': 0, 'blue': 0}

        # string manipulation to get game_no and results
        results = list(line.strip().split(':')[1].split('; '))

        # loop through results
        for result in results:
            ball_counts = list(result.split(', '))

            # for loop through number of balls for each result
            for count in ball_counts:
                amount, type = count.strip().split()

                # check if current result amount is greater than dictionary amount
                if int(amount) > mins[type]:
                    mins[type] = int(amount)

        # add products to total
        total += mins['red'] * mins['green'] * mins['blue']

    return total

print(day_2_2('aoc_2023/day_2/input.txt'))

from icecream import ic

def day_1_1(textfile):
    with open(textfile) as f:
        lines = f.readlines()

        total = 0
        for line in lines:
            digits = [x for x in line if x.isdigit()]
            total += int(digits[0] + digits[-1])
        return total

print(day_1_1('aoc_2023/day_1/input.txt'))

nums = {'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'}

def day_1_2(textfile):
    with open(textfile) as f:
        lines = f.readlines()

        total = 0

        for line in lines:

            # searching for the words from the dict
            for num in nums:

                # replacing second letter to allow for overlap e.g. 'oneight'
                if line.find(num) != -1:
                    i = line.find(num)
                    line = line[:i+1] + nums[num] + line[i + 2:]

                    # searching again from previous find point - gross but effective
                    # this could/should have been a recursion
                    if line.find(num, i) != -1:
                        i = line.find(num)
                        line = line[:i+1] + nums[num] + line[i + 2:]

                        # searching again from previous find point - gross but effective
                        # this could/should have been a recursion
                        if line.find(num, i) != -1:
                            i = line.find(num)
                            line = line[:i+1] + nums[num] + line[i + 2:]

            digits = [x for x in line if x.isdigit()]

            total += int(digits[0] + digits[-1])

        return total

print(day_1_2('aoc_2023/day_1/input.txt'))

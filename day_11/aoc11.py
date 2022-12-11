import operator
dictCalc = { "-": operator.sub, "/": operator.truediv,"+":operator.add,"*":operator.mul}

class Monkey():
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.items = []
        self.operation = []
        self.test = 0
        self.true = ''
        self.false = ''

def set_up_dict(lines):
    dct = {}
    current_monkey = ''
    for line in lines:
        splits = line.split(':')
        if splits[0][:-2] == 'Monkey':
            dct[splits[0]] = {'Counter':0}
            current_monkey = splits[0]
        if splits[0] == '  Starting items':
            dct[current_monkey][splits[0].strip()] = [int(x) for x in splits[1].split(',')]
        if splits[0] == '  Operation':
            dct[current_monkey][splits[0].strip()] = [x.strip('\n') for x in splits[1].split()]
        if splits[0] == '  Test':
            dct[current_monkey][splits[0].strip()] = int(splits[1].split()[-1])
        if splits[0] == '    If true':
            dct[current_monkey][splits[0].strip()] = f'Monkey {splits[1].split()[-1]}'
        if splits[0] == '    If false':
            dct[current_monkey][splits[0].strip()] = f'Monkey {splits[1].split()[-1]}'
    return dct

def day_11_1(input):

    with open(input) as f:
        lines = f.readlines()

    dct = set_up_dict(lines)

    for i in range(1,21):
        for monkey in dct.keys():
            # print(monkey)
            for item in dct[monkey]['Starting items']:
                dct[monkey]['Counter'] +=1
                # print(f'''{monkey} inspects an item with a worry level of {item}.''')
                worry = item
                changes = dct[monkey]['Operation'][2:]
                for idx, element in enumerate(changes):
                    if element in dictCalc:
                        if changes[idx+1] == 'old':
                            worry = dictCalc[element](worry, worry)
                        else:
                            worry = dictCalc[element](worry, int(changes[idx+1]))
                # print(f'''Worry level is changed by {' '.join(changes)} to {worry}.''')
                boredom = int(worry/3)
                # print(f'''{monkey} gets bored with item. Worry level is divided by 3 to {boredom}.''')
                if boredom % dct[monkey]['Test'] == 0:
                    # print(f'''Current worry level is divisible by {dct[monkey]['Test']}.''')
                    # print(f'''Item with worry level {boredom} is thrown to {dct[monkey]['If true']}.''')
                    dct[dct[monkey]['If true']]['Starting items'].append(boredom)
                else:
                    # print(f'''Current worry level is not divisible by {dct[monkey]['Test']}.''')
                    # print(f'''Item with worry level {boredom} is thrown to {dct[monkey]['If false']}.''')
                    dct[dct[monkey]['If false']]['Starting items'].append(boredom)
                # print('\n')
            dct[monkey]['Starting items'] = []
        # print(f'After round {i}, the monkeys are holding items with these worry levels:')
        # for monkey in dct.keys():
        #     print(f"{monkey}: {dct[monkey]['Starting items']}")

    counts = sorted([dct[monkey]['Counter'] for monkey in dct.keys()])
    print(counts[-2] * counts[-1])

# day_11_1('day_11/input.txt')

def day_11_2(input):

    with open(input) as f:
        lines = f.readlines()

    dct = set_up_dict(lines)

    for i in range(1,1001):
        for monkey in dct.keys():
            dct[monkey]['Counter'] += len(dct[monkey]['Starting items'])
            for item in dct[monkey]['Starting items']:
                worry = item
                changes = dct[monkey]['Operation'][2:]
                for idx, element in enumerate(changes):
                    if element in dictCalc:
                        if changes[idx+1] == 'old':
                            worry = dictCalc[element](worry, worry)
                        else:
                            worry = dictCalc[element](worry, int(changes[idx+1]))
                if worry % dct[monkey]['Test'] == 0:
                    dct[dct[monkey]['If true']]['Starting items'].append(worry)
                else:
                    dct[dct[monkey]['If false']]['Starting items'].append(worry)
            dct[monkey]['Starting items'] = []
        print(i)
        if i == 1 or i == 20 or i%1000 == 0:
            print(f'After round {i}:')
            for monkey in dct.keys():
                print(f"{monkey}: {dct[monkey]['Counter']}")

    counts = sorted([dct[monkey]['Counter'] for monkey in dct.keys()])
    print(counts[-2] * counts[-1])

day_11_2('day_11/test.txt')

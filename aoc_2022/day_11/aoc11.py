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

    def inspect(self, dct):
        for item in self.items:
            self.count +=1
            worry = item
            for idx, element in enumerate(self.operation):
                if element in dictCalc:
                    if self.operation[idx+1] == 'old':
                        worry = dictCalc[element](worry, worry)
                    else:
                        worry = dictCalc[element](worry, int(self.operation[idx+1]))
            boredom = int((worry)/(3))
            if boredom % self.test == 0:
                dct[self.true].items.append(boredom)
            else:
                dct[self.false].items.append(boredom)
        self.items = []

    def inspect2(self, dct):
        for item in self.items:
            self.count +=1
            worry = item
            for idx, element in enumerate(self.operation):
                if element in dictCalc:
                    if self.operation[idx+1] == 'old':
                        worry = dictCalc[element](worry, worry)
                    else:
                        worry = dictCalc[element](worry, int(self.operation[idx+1]))
            boredom = getSum(worry)
            if boredom % self.test == 0:
                dct[self.true].items.append(boredom)
            else:
                dct[self.false].items.append(boredom)
        self.items = []

def getSum(n):

    sum = 0
    for digit in str(n):
      sum += int(digit)
    return sum

def set_up_dict(lines):
    dct = {}
    current_monkey = ''
    for line in lines:
        splits = line.split(':')
        if splits[0][:-2] == 'Monkey':
            dct[splits[0]] = Monkey(splits[0])
            current_monkey = dct[splits[0]]
        if splits[0] == '  Starting items':
            current_monkey.items = [int(x) for x in splits[1].split(',')]
        if splits[0] == '  Operation':
            current_monkey.operation = [x.strip('\n') for x in splits[1].split()][2:]
        if splits[0] == '  Test':
            current_monkey.test = int(splits[1].split()[-1])
        if splits[0] == '    If true':
            current_monkey.true = f'Monkey {splits[1].split()[-1]}'
        if splits[0] == '    If false':
            current_monkey.false = f'Monkey {splits[1].split()[-1]}'
    return dct

def day_11_1(input):

    with open(input) as f:
        lines = f.readlines()

    dct = set_up_dict(lines)

    for i in range(1,21):
        for monkey in dct.keys():
            dct[monkey].inspect(dct)

    counts = sorted([dct[monkey].count for monkey in dct.keys()])
    print(counts[-2] * counts[-1])

day_11_1('day_11/test.txt')

def day_11_2(input):

    with open(input) as f:
        lines = f.readlines()

    dct = set_up_dict(lines)

    for i in range(1,21):
        for monkey in dct.keys():
            dct[monkey].inspect2(dct)
        print(i)
        if i == 1 or i == 20 or i%1000 == 0:
            print(f'After round {i}:')
            for monkey in dct.keys():
                print(f"{monkey}: {dct[monkey].count}")

    counts = sorted([dct[monkey].count for monkey in dct.keys()])
    print(counts[-2] * counts[-1])

day_11_2('day_11/test.txt')


# print(f'''{monkey} inspects an item with a worry level of {item}.''')
# print(f'''Worry level is changed by {' '.join(self.operation)} to {worry}.''')
# print(f'''{monkey} gets bored with item. Worry level is divided by 3 to {boredom}.''')
# print(f'''Current worry level is divisible by {self.test}.''')
# print(f'''Item with worry level {boredom} is thrown to {self.true}.''')
# print(f'''Current worry level is not divisible by {self.test}.''')
# print(f'''Item with worry level {boredom} is thrown to {self.false}.''')

def day_10_1(input):

    with open(input) as f:
        signals = f.readlines()

    X = 1
    cycle = 1

    cycle_dict = {}

    for signal in signals:
        # print(f'Cycle {cycle}')
        # print(signal.strip())
        if signal != 'noop\n':
            cycle_dict[cycle+1] = int(signal.split()[1])
            if cycle in cycle_dict.keys():
                X += cycle_dict[cycle]
        lst = [20,60,100, 140, 180, 220]
        if cycle in lst:
            print(f'X = {X}\n')
            print(f'Cycle {cycle} signal strength = {cycle*X}')
        cycle += 1
    print(cycle_dict)

day_10_1('day_10/test_2.txt')

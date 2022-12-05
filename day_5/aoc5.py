def day_5_1(crates_file, orders_file):

    with open(crates_file) as f:
        crates = f.readlines()

    piles = {}
    for c in crates:
        x = 1
        for i in range(1, len(c), 4):
            piles.setdefault(x,[]).append(c[i])
            x +=1

    for i in range(1,10):
        piles[i] = [x for x in piles[i][::-1] if x != ' ']

    with open(orders_file) as f:
        orders = f.readlines()

    for o in orders:
        s = o.split()
        for i in range(int(s[1])):
            piles[int(s[5])].append(piles[int(s[3])].pop())

    print(''.join(piles[i][-1] for i in range(1,10)))

day_5_1('day_5/crates.txt', 'day_5/orders.txt')


def day_5_2(crates_file, orders_file):

    with open(crates_file) as f:
        crates = f.readlines()

    piles = {}
    for c in crates:
        x = 1
        for i in range(1, len(c), 4):
            piles.setdefault(x,[]).append(c[i])
            x +=1

    for i in range(1,10):
        piles[i] = piles[i][:-1]
        piles[i] = [x for x in piles[i][::-1] if x != ' ']

    with open(orders_file) as f:
        orders = f.readlines()

    for o in orders:
        s = o.split()
        pile = int(s[1])
        original = int(s[3])
        new = int(s[5])
        piles[new] += piles[original][-pile:]
        piles[original] = piles[original][:-pile]

    print(''.join(piles[i][-1] if piles[i] else ' ' for i in range(1,10)))

day_5_2('day_5/crates.txt', 'day_5/orders.txt')

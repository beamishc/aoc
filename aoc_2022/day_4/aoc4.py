def day_4(input):

    with open(input) as f:
        pairs = f.readlines()

    overlap = 0

    for pair in pairs:
        a, b = pair.split(',')
        a, b = a.split('-'), b.split('-')

        a1, a2 = int(a[0]), int(a[1])
        b1, b2 = int(b[0]), int(b[1])

        if b1 <= a1 <= b2 or b1 <= a2 <= b2 or a1 <= b1 <= a2 or a1 <= b2 <= a2:
            overlap += 1

    print(overlap)

day_4('day_4/input.txt')

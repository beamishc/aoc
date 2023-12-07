from icecream import ic

with open('day_5/test_1.txt') as f:
    maps = f.read().split('\n\n')
    ic(maps)
    seeds, maps = maps[0].split()[1:], maps[1:]
    ic(maps)
    ic(seeds)
    for i, m in enumerate(maps):
        ic(m)
        maps[i] = m.strip().split('\n')[1:]
        maps[i] = [[[s, s + r], [d, d + r]]
                        for d, s, r in [map(int, x.split()) for x in maps[i]]]


ic(maps)
ic(seeds)

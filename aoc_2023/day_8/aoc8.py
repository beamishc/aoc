from icecream import ic

def day_8_1(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')
        dirs,nodes = lines[0].strip(), lines[2:]

        # make list of dirs so that L = 0 and R = 1
        ds = [0 if x == 'L' else 1 for x in dirs]

        node_dct = {}
        for node in nodes:
            k, v = node.split(' = ')
            node_dct[k] = (v[1:4], v[6:9])

        # create
        past_ds, len_ds, current_ds = [], 0, ds[0]
        past, current = [], 'AAA'

        while current != 'ZZZ':
            # ic(current, dirs[len_ds])
            past.append(current)
            past_ds.append(current_ds)
            current = node_dct[current][current_ds]
            len_ds += 1
            if len_ds >= len(ds):
                len_ds = 0
            current_ds = ds[len_ds]
        return len(past)

ic(day_8_1('day_8/input.txt'))

def day_8_2(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')
        dirs,nodes = lines[0].strip(), lines[2:]

        # make list of dirs so that L = 0 and R = 1
        ds = [0 if x == 'L' else 1 for x in dirs]

        # create
        past_ds = []
        len_ds = 0
        current_ds = ds[0]
        past = []
        current = []

        node_dct = {}
        for node in nodes:
            k, v = node.split(' = ')
            node_dct[k] = (v[1:4], v[6:9])
            if k[-1] == 'A':
                current.append(k)
        i=0
        while sum([x[-1] == 'Z' for x in current]) != len(current):
            ic(i)
            past.append(current)
            past_ds.append(current_ds)
            current = [node_dct[c][current_ds] for c in current]
            len_ds += 1
            if len_ds >= len(ds):
                len_ds = 0
            current_ds = ds[len_ds]
            i+=1
        return len(past)

ic(day_8_2('day_8/input.txt'))

# oli suggests lowest common multiples

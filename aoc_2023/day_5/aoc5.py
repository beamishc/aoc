from icecream import ic

def day_5_1(textfile):
    with open(textfile) as f:
        # lines = f.readlines()
        lines = f.read().split('\n\n')
    seeds = [int(x) for x in lines[0].split()[1:]]
    mapped_seeds = {}
    original_seeds = [seeds]
    for seed in seeds:
        mapped_seeds[seed] = 0
    i=1
    for line in lines[1:]:
        map_type, ranges = line.split(' map:\n')
        ranges = ranges.strip().split('\n')
        ranges = [[int(x) for x in e.split()] for e in ranges]
        ic(ranges)

        # i+=1
        # if i > 2:
        #     ic(i, mapped_seeds)
        #     new_lst = [v for k,v in mapped_seeds.items()]
        #     original_seeds.append(new_lst)
        #     mapped_seeds = {}
        #     for x in new_lst:
        #         mapped_seeds[x] = 0
        # ic(i, mapped_seeds)
        for r in ranges:
            now, then, r_l = r[0], r[1], r[2]
            now_start = (now, now + r_l)
            # now_next = (now + r_l, now + r_l*2)
            then_start =  (then, then + r_l)
            # then_next = (then + r_l, then + r_l*2)

            ic(then_start, now_start)

            for seed in original_seeds[i-2]:
                if seed >= now_start[0] and seed <= now_start[1]:
                    ic(i, seed, 'in now_start')
                    # ic(now_start[-1] - seed - 1)
                    mapped_seeds[seed] = then_start[-now_start[-1] + seed - 1]
                    # ic(mapped_seeds)
                # elif seed in now_next:
                    # ic(i, seed, 'in now_next')
                    # ic(now_next[-1] - seed - 1)
                    # mapped_seeds[seed] = then_next[-now_next[-1] + seed - 1]
                    # ic(mapped_seeds)
                else:
                    mapped_seeds[seed] = seed

    # seed_rounds[i] = mapped_seeds.values()


    # ic(mapped_seeds)
    # ic(seed_rounds)



print(day_5_1('day_5/test_1.txt'))


# seeds = [int(x) for x in digits.strip().split()]
# map_dct[1] = {'values':{k:v for k, v in zip(range(1,101), range(1,101))}}
# ic(line.split()[0].split('-'))
# what_num[line.split()[0]] = str(i) + '_' + line.split()[0].split('-')[2]
# map_dct[i] = {'values':{k:v for k, v in zip(range(1,101), range(1,101))}}
# map_dct[i] = [int(x) for x in line.strip().split()]



                # if seed in then_start:
                #     ic(i, seed, 'in then_start')
                # elif seed in dest_after:
                #     ic(i, seed, 'in dest_after')

def day_1(textfile):
    with open(textfile) as f:
        lines = f.readlines()
    dct = {}
    counter = 1
    for row in lines:
        try:
            int(row)
            dct.setdefault(counter, 0)
            dct[counter] += int(row)
        except:
            counter += 1
    return dct

final = day_1('day_1/input.txt')
sorted_final = sorted(final.values())
print(sum(sorted_final[-3:]))

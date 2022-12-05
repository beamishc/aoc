def day_1(textfile):
    with open(textfile) as f:
        lines = f.readlines()
    dct = {}
    counter = 1
    for row in lines:
        try:
            int(row)
            if counter in dct.keys():
                dct[counter]+=int(row)
            else:
                dct[counter] = int(row)
        except:
            counter += 1
    return dct

final = day_1('input.txt')
sorted_final = sorted(final.values())
print(sum(sorted_final[-3:]))

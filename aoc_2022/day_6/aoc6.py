def day_6_1(input):

    with open(input) as f:
        datastream = f.readlines()

    for i in range(len(datastream[0])):
        if len(set(datastream[0][i:i+4])) == 4:
            print(i+4)
            break

day_6_1('day_6/input.txt')

def day_6_2(input):

    with open(input) as f:
        datastream = f.readlines()

    for i in range(len(datastream[0])):
        if len(set(datastream[0][i:i+14])) == 14:
            print(i+14)
            break

day_6_2('day_6/input.txt')

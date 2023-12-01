def day_13_1(input):

    with open(input) as f:
        packets = f.readlines()

    left = [packet.strip() for packet in packets[::3]]

    right = [packet.strip() for packet in packets[1::3]]


    # print(list(zip(left, right)))

    for i, packet in enumerate(left):
        l = eval(packet)
        r = eval(right[i])
        if l:
            if type(l[0]) == list:
                if type(r[0]) == list:
                    for i, x in enumerate(l[0]):
                        if x <= r[0][i]:
                            print('Samesies')
                        else:
                            print('Oh no')
        print (eval(packet), ' v ', eval(right[i]))



day_13_1('day_13/test.txt')

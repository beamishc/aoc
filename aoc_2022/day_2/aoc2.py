def day_2(input):
    with open(input) as f:
        lines = f.readlines()
    dct = {'A': {'X':'Scissors', 'Y': 'Rock', 'Z': 'Paper'}
           , 'B': {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
           , 'C': {'X': 'Paper', 'Y': 'Scissors', 'Z': 'Rock'}
           , 'X': 0
           , 'Y': 3
           , 'Z': 6
           , 'Rock': 1
           , 'Paper': 2
           , 'Scissors': 3
           }
    score = 0
    for row in lines:
        them = dct[row[0]]
        me = row[2]
        which = dct[them[me]]
        score += which + dct[me]
    print(score)

day_2('day_2/input.txt')

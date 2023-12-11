from icecream import ic

def day_11_1(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('/\/n')

ic(day_11_1('day_11/test_1.txt'))

def day_11_2(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('/\/n')

ic(day_11_2('day_11/test_2.txt'))

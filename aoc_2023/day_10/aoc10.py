from icecream import ic
import numpy as np

dct = {'|': 'ns',
       '-': 'ew',
       'L': 'ne',
       'J': 'nw',
       '7': 'sw',
       'F': 'se',
       'S': 0}

def day_10_1(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')
        for i, line in enumerate(lines):
            lines[i] = [dct[x] if x in dct.keys() else x for x in line]
        max = len(lines[0]) - 1
        pipe_grid = np.array(lines)
        ic(pipe_grid)

        for i, pipe in np.ndenumerate(pipe_grid):
            if pipe != '.':
                ic(i, pipe)
                e,w,n,s = False, False, False, False
                if 'e' in pipe and i[1] != max:
                    if pipe_grid[i[0],(i[1]+1):][0] != '.':
                        e = True
                if 'w' in pipe and i[1] != 0:
                    if pipe_grid[i[0],:i[1]][::-1][0] != '.':
                        w = True
                if 'n' in pipe and i[0] != 0:
                    if pipe_grid[:i[0],i[1]][::-1][0] != '.':
                        n = True
                if 's' in pipe and i[0] != max:
                    if pipe_grid[(i[0]+1):,i[1]][0] != '.':
                        s = True
                ic(e, w, n, s)
                if sum([e,w,n,s]) >=2:
                    pipe_grid[i] = 'RP'



        ic(pipe_grid)

ic(day_10_1('day_10/test_2.txt'))

def day_10_2(textfile):
    with open(textfile) as f:
        lines = f.read().strip().split('\n')

ic(day_10_2('day_10/test_2.txt'))

import numpy as np
t_unique = []

def t_u(t_row, t_col):
    if [t_row,t_col] not in t_unique:
        t_unique.append([t_row,t_col])

def day_9_1(input):

    with open(input) as f:
        instructions = f.readlines()

    h_row, h_col = 4, 0
    t_row, t_col = 4, 0
    grid = np.full((6, 6), '.')
    for line in instructions:
        print(line.strip())
        direction = line[0]
        distance = int(line[2:].strip())

        for i in range(1,distance+1):
            if direction == 'L':
                h_col -= 1
                if t_col >= (h_col + 1):
                    t_col -= 1
                    if t_row != (h_row):
                        t_row = h_row
                grid[t_row, t_col] = f'T{i}'
                grid[h_row, h_col] = f'H{i}'
                print('H = [',h_row,',', h_col, ']')
                print('T = [',t_row,',', t_col, ']\n')
                print(grid, '\n')
            if direction == 'R':
                h_col += 1
                if t_col <= (h_col - 2):
                    t_col += 1
                grid[t_row, t_col] = f'T{i}'
                grid[h_row, h_col] = f'H{i}'
                print('H = [',h_row,',', h_col, ']')
                print('T = [',t_row,',', t_col, ']\n')
                print(grid, '\n')
            if direction == 'U':
                h_row -= 1
                if t_row >= (h_row + 2):
                    t_row -= 1
                    if t_col != (h_col):
                        t_col = h_col
                grid[t_row, t_col] = f'T{i}'
                grid[h_row, h_col] = f'H{i}'
                print('H = [',h_row,',', h_col, ']')
                print('T = [',t_row,',', t_col, ']\n')
                print(grid, '\n')
            if direction == 'D':
                h_row += 1
                if t_row <= (h_row - 2):
                    t_row += 1
                grid[t_row, t_col] = f'T{i}'
                grid[h_row, h_col] = f'H{i}'
                print('H = [',h_row,',', h_col, ']')
                print('T = [',t_row,',', t_col, ']\n')
                print(grid, '\n')
            t_u(t_row, t_col)
        # print('[',h_row,',', h_col, ']\n')
        # print('[',t_row,',', t_col, ']\n')
    # print('\n'.join(str(x) for x in t_unique))
    print(len(t_unique))

day_9_1('day_9/test.txt')

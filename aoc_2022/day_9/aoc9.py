import numpy as np
t_unique = []
tail_unique = []

def t_u(t_row, t_col, lst):
    if [t_row,t_col] not in lst:
        lst.append([t_row,t_col])

def clear(grid,t_row,t_col):
    grid[t_row, t_col] = '.'

def update(grid,t_row,t_col, h_row, h_col):
    grid[t_row, t_col] = f'1'
    grid[h_row, h_col] = f'H'

def update2(grid,i, t_row, t_col):
    grid[t_row, t_col] = f'{i}'

def day_9_1(input):

    with open(input) as f:
        instructions = f.readlines()

    h_row, h_col = 0, 0
    t_row, t_col = 0, 0

    for line in instructions:
        direction = line[0]
        distance = int(line[2:].strip())
        for i in range(1,distance+1):

            if direction == 'L':
                h_col -= 1
                if t_col >= (h_col + 2):
                    t_col -= 1
                    if t_row != (h_row):
                        t_row = h_row

            if direction == 'R':
                h_col += 1
                if t_col <= (h_col - 2):
                    t_col += 1
                    if t_row != (h_row):
                        t_row = h_row

            if direction == 'U':
                h_row -= 1
                if t_row >= (h_row + 2):
                    t_row -= 1
                    if t_col != (h_col):
                        t_col = h_col

            if direction == 'D':
                h_row += 1
                if t_row <= (h_row - 2):
                    t_row += 1
                    if t_col != (h_col):
                        t_col = h_col

            t_u(t_row, t_col, t_unique)
    print(len(t_unique))

day_9_1('day_9/input.txt')


def day_9_2(input):

    with open(input) as f:
        instructions = f.readlines()

    row = {k:v for k,v in zip(range(0,10), [15]*10)}
    col = {k:v for k,v in zip(range(0,10), [11]*10)}

    t_u(row[9], col[9], tail_unique)

    grid = np.full((21, 26), '.')
    for line in instructions:
        print(line.strip())
        direction = line[0]
        distance = int(line[2:].strip())
        for step in range(1,distance+1):

            if direction == 'L':
                col[0] -= 1
                update2(grid,0,row[0],col[0])
                for i in range(1,9):
                    # clear(grid,row[i],col[i])
                    if col[i] >= (col[i-1] + 2):
                        col[i] -= 1
                        if row[i] != (row[i-1]):
                            row[i] = row[i-1]
                            if row[i] <= (row[i+1] - 2):
                                row[i] += 1
                    update2(grid,i,row[i],col[i])

                if col[9] >= (col[8] + 2):
                    col[9] -= 1
                    if row[9] != (row[8]):
                        row[9] = row[8]
                update2(grid,9,row[9],col[9])
                # print(row)
                # print(col)
                # print(grid, '\n')
                for row in grid:
                    temp = row
                    print(''.join(temp))

            if direction == 'R':
                col[0] += 1
                update2(grid,0,row[0],col[0])
                for i in range(1,9):
                    # clear(grid,row[i],col[i])
                    if col[i] <= (col[i-1] - 2):
                        col[i] += 1
                        if row[i] != (row[i-1]):
                            row[i] = row[i-1]
                            if row[i] >= (row[i+1] + 2):
                                row[i] -= 1
                    update2(grid,i,row[i],col[i])

                if col[9] <= (col[8] - 2):
                    col[9] += 1
                    if row[9] != (row[8]):
                        row[9] = row[8]
                update2(grid,9,row[9],col[9])
                # print(row)
                # print(col)
                # print(grid, '\n')
                # for row in grid:
                #     temp = row
                #     print(''.join(temp))

            if direction == 'U':
                row[0] -= 1
                update2(grid,0,row[0],col[0])
                for i in range(1,9):
                    # clear(grid,row[i],col[i])
                    if row[i] >= (row[i-1] + 2):
                        row[i] -= 1
                        if col[i] != (col[i-1]):
                            col[i] = col[i-1]
                            if col[i] >= (col[i+1] + 2):
                                col[i] -= 1
                    update2(grid,i,row[i],col[i])

                if row[9] >= (row[8] + 2):
                    row[9] -= 1
                    if col[9] != (col[8]):
                        col[9] = col[8]
                update2(grid,9,row[9],col[9])
                # print(row)
                # print(col)
                # for row in grid:
                #     temp = row
                #     print(''.join(temp))

            if direction == 'D':
                row[0] += 1
                update2(grid,0,row[0],col[0])
                for i in range(1,9):
                    # clear(grid,row[i],col[i])
                    if row[i] <= (row[i-1] - 2):
                        row[i] += 1
                        if col[i] != (col[i-1]):
                            col[i] = col[i-1]
                            if col[i] <= (col[i+1] - 2):
                                col[i] += 1
                    update2(grid,i,row[i],col[i])

                if row[9] <= (row[8] - 2):
                    row[9] += 1
                    if col[9] != (col[8]):
                        col[9] = col[8]
                update2(grid,9,row[9],col[9])
                # print(row)
                # print(col)
                # print(grid, '\n')
                for row in grid:
                    temp = row
                    print(''.join(temp))
            t_u(row[9], col[9], tail_unique)
        # for i in range(0,10):
        #     update2(grid,i,row[i],col[i])
    print(len(tail_unique))
    print(tail_unique)
    for row in grid:
        print(''.join(row))

day_9_2('day_9/test2.txt')

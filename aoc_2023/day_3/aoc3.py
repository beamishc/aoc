from icecream import ic
from functools import reduce
import numpy as np

# Creating a quick function to check if any direction was a symbol
def is_symbol(direction):
    if len(direction) > 0:
        if direction[0] != '.' and not direction[0].isdigit():
            return True
    return False

# Creating a quick function for part 2 to check if any direction was a digit
# (in a way that was more useful immediately to me than .isdigit() because of the inclusion of the if statement)
def is_dig(direction):
    if len(direction) > 0:
        if direction[0].isdigit():
            return True
    return False

# Got halfway through part 1 and wished I'd done a recursion, but oh well...
def day_3_1(textfile):

    # getting the info out of the text file and into a np.array
    with open(textfile) as f:
        lines = f.readlines()

    part_list = []
    for parts in lines:
        part_list.append([part for part in parts.strip()])

    part_grid = np.array(part_list)

    # variables of the edges
    maxs = part_grid.shape
    max_row = maxs[0] - 2
    max_col = maxs[1] - 2

    nums = []

    for i, part in np.ndenumerate(part_grid):

        # why do any work if it isn't a digit? Thinking with my brain here
        if part.isdigit():

            # getting a list of every thing in each compass direction from the coord
            N = part_grid[:i[0],i[1]][::-1]
            E = part_grid[i[0],:i[1]][::-1]
            S = part_grid[(i[0]+1):,i[1]]
            W = part_grid[i[0],(i[1]+1):]

            # setting default values for the diagonal points
            NE, NW, SW, SE = ['.', '.', '.', '.']

            # checking diagonals were valid at edges
            if i[0] > 0 and i[1] < max_col:
                NE = [part_grid[i[0]-1][i[1]+1]]

            if i[0] > 0 and i[1] > 0:
                NW = [part_grid[i[0]-1][i[1]-1]]

            if i[0] < max_row and i[1] < max_col:
                SW = [part_grid[i[0]+1][i[1]-1]]

            if i[0] < max_row and i[1] < max_col:
                SE = [part_grid[i[0]+1][i[1]+1]]

            # creating a list of all the compass lists to feed into the for loop
            directions = [E, NE, SE, W, NW, SW, N, S]

            # setting up number to be manipulated
            relevant_num = part

            # looping through compass lists to check for symbols
            # if any symbols, then continue
            if sum([is_symbol(direction) for direction in directions]) > 0:
                # loop through east and add any digits to left, else break
                for e in E:
                    if e.isdigit():
                        relevant_num = e + relevant_num
                    else:
                        break
                # loop through west and add any digits to right, else break
                for w in W:
                    if w.isdigit():
                        relevant_num = relevant_num + w
                    else:
                        break

                # check that number isn't already in master list, then append
                if len(nums) >0:
                    if int(relevant_num) != nums[-1]:
                        nums.append(int(relevant_num))
                else:
                    nums.append(int(relevant_num))
    return sum(nums)


print(day_3_1('aoc_2023/day_3/input.txt'))

def day_3_2(textfile):
    with open(textfile) as f:
        lines = f.readlines()

    part_list = []
    for parts in lines:
        part_list.append([part for part in parts.strip()])

    part_grid = np.array(part_list)
    maxs = part_grid.shape
    max_row = maxs[0] - 2
    max_col = maxs[1] - 2

    final_nums = 0

    for i, part in np.ndenumerate(part_grid):
        if part == '*':

            N = list(part_grid[:i[0],i[1]][::-1])
            E = list(part_grid[i[0],(i[1]+1):])
            S = list(part_grid[(i[0]+1):,i[1]])
            W = list(part_grid[i[0],:i[1]][::-1])

            NE, NW, SW, SE = ['.', '.', '.', '.']

            if i[0] > 0 and i[1] < max_col:
                NE = [part_grid[i[0]-1][i[1]+1]]

            if i[0] > 0 and i[1] > 0:
                NW = [part_grid[i[0]-1][i[1]-1]]

            if i[0] < max_row+1 and i[1] < max_col:
                SW = [part_grid[i[0]+1][i[1]-1]]

            if i[0] < max_row+1 and i[1] < max_col:
                SE = [part_grid[i[0]+1][i[1]+1]]

            directions = [N, NE, E, SE, S, SW, W, NW]
            direction_names = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
            results = [is_dig(direction) for direction in directions]

            gear_nums = []

            if sum(results) > 1:
                dir_is_dig = [direction_names[i] for i in range(len(results))if results[i] == True]

                for dir in dir_is_dig:
                    if dir == 'N':
                        i_col, i_row = i[0]-1, i[1]
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'NE':
                        i_col, i_row = i[0]-1, i[1]+1
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'E':
                        i_col, i_row = i[0], i[1]+1
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'SE':
                        i_col, i_row = i[0]+1, i[1]+1
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'S':
                        i_col, i_row = i[0]+1, i[1]
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'SW':
                        i_col, i_row = i[0]+1, i[1]-1
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'W':
                        i_col, i_row = i[0], i[1]-1
                        part_dig = part_grid[i_col][i_row]
                    if dir == 'NW':
                        i_col, i_row = i[0]-1, i[1]-1
                        part_dig = part_grid[i_col][i_row]

                    E = part_grid[i_col,:i_row][::-1]
                    W = part_grid[i_col,(i_row+1):]

                    relevant_num = part_dig

                    for e in E:
                        if e.isdigit():
                            relevant_num = e + relevant_num
                        else:
                            break
                    for w in W:
                        if w.isdigit():
                            relevant_num = relevant_num + w
                        else:
                            break
                    if len(gear_nums) > 0:
                        if int(relevant_num) not in gear_nums:
                            gear_nums.append(int(relevant_num))
                    else:
                        gear_nums.append(int(relevant_num))
            if len(gear_nums) > 1:
                final_nums += reduce(lambda x, y: x*y, gear_nums)

    return final_nums

print(day_3_2('aoc_2023/day_3/input.txt'))

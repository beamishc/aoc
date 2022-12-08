import numpy as np
def day_8_1(input):

    with open(input) as f:
        forest = f.readlines()

    forest_list = []
    for trees in forest:
        forest_list.append([int(tree) for tree in trees.strip()])

    forest_grid = np.array(forest_list)
    visible = 0

    for i, tree in np.ndenumerate(forest_grid):
        left = all(x < tree for x in forest_grid[i[0],:i[1]])
        right = all(x < tree for x in forest_grid[i[0],(i[1]+1):])
        up = all(x < tree for x in forest_grid[:i[0],i[1]])
        down = all(x < tree for x in forest_grid[(i[0]+1):,i[1]])
        if (left + right + up + down) >= 1:
            visible += 1
    print(visible)

day_8_1('day_8/input.txt')

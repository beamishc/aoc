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

def day_8_2(input):

    with open(input) as f:
        forest = f.readlines()

    forest_list = []
    for trees in forest:
        forest_list.append([int(tree) for tree in trees.strip()])

    forest_grid = np.array(forest_list)
    scenic = []

    for i, tree in np.ndenumerate(forest_grid):
        left = forest_grid[i[0],:i[1]][::-1]
        right = forest_grid[i[0],(i[1]+1):]
        up = forest_grid[:i[0],i[1]][::-1]
        down = forest_grid[(i[0]+1):,i[1]]
        end = 1
        view = {
            'left': {'len':len(left), 'cutoff':[n for n,i in enumerate(left) if i >= tree]},
            'right': {'len':len(right), 'cutoff':[n for n,i in enumerate(right) if i >= tree]},
            'up': {'len':len(up), 'cutoff':[n for n,i in enumerate(up) if i >= tree]},
            'down': {'len':len(down), 'cutoff':[n for n,i in enumerate(down) if i >= tree]},
            }
        for direction in view.keys():
            if view[direction]['len'] == 0:
                end = 0
            if not view[direction]['cutoff'] and view[direction]['len'] > 0:
                end = end * view[direction]['len']
            if view[direction]['cutoff']:
                end = end * (view[direction]['cutoff'][0] + 1)
        scenic.append(end)
    print(max(scenic))

day_8_2('day_8/input.txt')

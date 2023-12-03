import numpy as np
import networkx as nx
def day_12_1(input):

    with open(input) as f:
        grid = f.readlines()

    map = np.array([[x for x in row.strip()] for row in grid])
    print(map)
    g = nx.DiGraph()
    print(g)

    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter == "S":
                start = (i, j)
                val = 0
            elif letter == "E":
                end = (i, j)
                val = 25
            else:
                val = ord(letter) - ord("a")
            g.add_node((i, j), val=val)

    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            current = i, j
            neighbors = [(i+1, j),
                        (i-1, j),
                        (i, j+1),
                        (i, j-1)]

            for n in neighbors:
                if n in g.nodes and g.nodes.get(n)['val'] <= g.nodes.get(current)['val'] + 1:
                        g.add_edge(current, n)

    result = nx.shortest_path(g, start, end)
    print(result)
    print(len(result)-1)

    print(g)

    for index in result:
        map[index] = 'X'

    print(map)
day_12_1('aoc_2022/day_12/input.txt')




# result = nx.shortest_path(g, start, end)
# print(len(result)-1)
# ​
# result2 = []
# ​
# for n in g.nodes():
#     if g.nodes.get(n)['val'] == 0:
#         try:
#             result2.append(len(nx.shortest_path(g, n, end)))
#         except:
#             pass

# print(min(result2)-1)

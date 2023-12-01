def day_18_1(input):

    with open(input) as f:
        cubes = f.readlines()

    for cube in cubes:
        x, y ,z = [int(num) for num in cube.strip().split(',')]

day_18_1('day_18/test.txt')

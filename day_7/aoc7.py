def day_7_1(input):

    with open(input) as f:
        tree = f.readlines()

    dir_dict = {}
    dir_list = ['']

    for line in tree:

        command = line[:4]
        location = line[5:].strip()
        dir_name = line[4:].strip()

        if command == "$ cd" and location != "..":
            dir_list.append(location)
            dir_dict.setdefault(''.join(dir_list), {'contains':[], 'size': 0})

        elif line.strip() == "$ cd ..":
            dir_list.pop()

        elif command == "dir ":
            parent = ''.join(dir_list)
            new_dir = parent + dir_name
            dir_dict.setdefault(new_dir, {'contains':[], 'size': 0})
            dir_dict[parent]['contains'].append(new_dir)

        elif command == "$ ls":
            continue

        else:
            result = line.split()
            dir_dict[''.join(dir_list)]['size'] += int(result[0])

    final_dict = {}

    for dir, vals in reversed(dir_dict.items()):
        final_dict[dir] = int(dir_dict[dir]['size']) + sum(int(final_dict[contained]) for contained in dir_dict[dir]['contains'])

    print(sum(num for num in final_dict.values() if num <= 100000))

day_7_1('day_7/input.txt')

def day_7_2(input):

    with open(input) as f:
        tree = f.readlines()

    dir_dict = {}
    dir_list = ['']

    for line in tree:

        command = line[:4]
        location = line[5:].strip()
        dir_name = line[4:].strip()

        if command == "$ cd" and location != "..":
            dir_list.append(location)
            dir_dict.setdefault(''.join(dir_list), {'contains':[], 'size': 0})

        elif line.strip() == "$ cd ..":
            dir_list.pop()

        elif command == "dir ":
            parent = ''.join(dir_list)
            new_dir = parent + dir_name
            dir_dict.setdefault(new_dir, {'contains':[], 'size': 0})
            dir_dict[parent]['contains'].append(new_dir)

        elif command == "$ ls":
            continue

        else:
            result = line.split()
            dir_dict[''.join(dir_list)]['size'] += int(result[0])

    final_dict = {}

    for dir, vals in reversed(dir_dict.items()):
        final_dict[dir] = int(dir_dict[dir]['size']) + sum(int(final_dict[contained]) for contained in dir_dict[dir]['contains'])

    total = 70000000
    used = sum(int(dir_dict[dir]['size']) for dir in dir_dict)
    unused = total - used
    need = 30000000 - unused

    print(min(num for num in final_dict.values() if num >= need))

day_7_2('day_7/input.txt')

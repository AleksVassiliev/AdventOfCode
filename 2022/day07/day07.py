def restore_tree(commands):
    cur_path = []
    cur_dir = ''
    dir_size = {}
    for line in commands:
        if line[0] == '$':
            args = line.split(' ')
            if args[1] == 'cd':
                if (args[2] == '..'):
                    cur_path.pop(-1)
                else:
                    cur_path.append(args[2])
            elif args[1] == 'ls':
                cur_dir = '_'.join(cur_path)
                dir_size[cur_dir] = 0
        elif line.startswith('dir'):
            dir_name = line.split(' ')[1]
            dir_size[cur_dir + f'_{dir_name}'] = 0
        else:
            dir_size[cur_dir] += int(line.split(' ')[0])
    for key in dir_size:
        path = key.split('_')
        while len(path) > 1:
            parent = '_'.join(path[:-1])
            dir_size[parent] += dir_size[key]
            path = path[:-1]
    return dir_size


def calculate_size_v1(commands):
    dir_size = restore_tree(commands)
    total_size = 0
    for key in dir_size:
        if dir_size[key] <= 100000:
            total_size += dir_size[key]
    return total_size


def calculate_size_v2(commands):
    dir_size = restore_tree(commands)
    to_delete = []
    free_space = 70000000 - dir_size['/']
    for key in dir_size:
        if (free_space + dir_size[key]) >= 30000000:
            to_delete.append(dir_size[key])
    return min(to_delete)


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = calculate_size_v1(data)
    print(result_v1)
    result_v2 = calculate_size_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

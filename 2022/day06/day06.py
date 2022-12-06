def find_marker(data, sz):
    for i in range(len(data) - sz):
        s = data[i:i+sz]
        if len(set(s)) == sz:
            return (i + sz)


def find_marker_v1(data):
    return find_marker(data, 4)


def find_marker_v2(data):
    return find_marker(data, 14)


def main():
    with open('./input.txt') as fi:
        data = fi.readline()
        result_v1 = find_marker_v1(data)
        print(result_v1)
        result_v2 = find_marker_v2(data)
        print(result_v2)


if __name__ == '__main__':
    main()

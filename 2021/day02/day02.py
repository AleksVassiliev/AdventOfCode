def calculate_position_v1(course: list):
    pos_h = 0
    pos_v = 0
    for line in course:
        direction, value = line.split(' ')
        value = int(value)
        if direction == 'forward':
            pos_h += value
        elif direction == 'down':
            pos_v += value
        elif direction == 'up':
            pos_v -= value
    return (pos_h * pos_v)


def calculate_position_v2(course: list):
    pos_h = 0
    pos_v = 0
    aim = 0
    for line in course:
        direction, value = line.split(' ')
        value = int(value)
        if direction == 'forward':
            pos_h += value
            pos_v += (value * aim)
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value
    return (pos_h * pos_v)


def main():
    course = [line for line in open('./input02.txt')]
    result_v1 = calculate_position_v1(course)
    print(result_v1)
    result_v2 = calculate_position_v2(course)
    print(result_v2)


if __name__ == '__main__':
    main()

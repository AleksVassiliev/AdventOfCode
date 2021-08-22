def calculate_distance_v1(data):
    directions = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    rotations = {
        'L90': {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'},
        'L180': {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'},
        'L270': {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'},
        'R90': {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'},
        'R180': {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'},
        'R270': {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'}
    }

    pos_x = 0
    pos_y = 0
    pos_dir = (1, 0)
    facing = 'E'

    for line in data:
        direction = line[0]
        value = int(line[1:])
        if direction == 'F':
            pos_dir = directions[facing]
        elif direction in ['N', 'S', 'E', 'W']:
            pos_dir = directions[direction]
        elif direction in ['L', 'R']:
            facing = rotations[line][facing]
            pos_dir = (0, 0)
        pos_x += pos_dir[0] * value
        pos_y += pos_dir[1] * value

    return abs(pos_x) + abs(pos_y)


def calculate_distance_v2(data):
    directions = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    pos_ship = (0, 0)
    pos_waypoint = (10, 1)

    for line in data:
        direction = line[0]
        value = int(line[1:])
        if direction == 'F':
            x = pos_ship[0] + value * pos_waypoint[0]
            y = pos_ship[1] + value * pos_waypoint[1]
            pos_ship = (x, y)
        elif direction in ['N', 'S', 'E', 'W']:
            x = pos_waypoint[0] + value * directions[direction][0]
            y = pos_waypoint[1] + value * directions[direction][1]
            pos_waypoint = (x, y)
        elif direction in ['L', 'R']:
            if line in ['L90', 'R270']:
                pos_waypoint = (-pos_waypoint[1], pos_waypoint[0])
            elif line in ['L180', 'R180']:
                pos_waypoint = (-pos_waypoint[0], -pos_waypoint[1])
            elif line in ['L270', 'R90']:
                pos_waypoint = (pos_waypoint[1], -pos_waypoint[0])

    return abs(pos_ship[0]) + abs(pos_ship[1])



def main():
    data = [line.strip() for line in open('./input12.txt')]
    result_v1 = calculate_distance_v1(data)
    print(result_v1)
    result_v2 = calculate_distance_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

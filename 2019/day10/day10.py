import math

def count_asteroids(data, x0, y0):
    angles = set()
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell == '#':
                angle = math.atan2(x0-x, y0-y) * 180 / math.pi
                if angle < 0:
                    angle += 360
                angles.add(angle)
    return len(angles)


def main():
    data = [ x.rstrip('\n') for x in open('input10') ]

    result = 0
    for j, line in enumerate(data):
        for i, cell in enumerate(line):
            if cell == '#':
                res = count_asteroids(data, i, j)
                result = max(res, result)
    print(result)

    
if __name__ == '__main__':
    main()

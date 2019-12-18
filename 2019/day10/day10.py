import math
import collections


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


def destroy_asteroids(data, x0, y0):
    asteroids = collections.defaultdict(list)
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell == '#':
                angle = math.atan2(x0-x, y0-y) * 180 / math.pi
                if angle <= 0:
                    angle += 360
                distance = math.sqrt(pow(x0-x, 2) + pow(y0-y, 2))
                if (x0 != x) or (y0 != y):
                    asteroids[angle].append((x, y, distance))
    for k in asteroids:
        asteroids[k].sort(key=lambda x: x[2])
    
    angles = list(asteroids.keys())
    angles.sort(reverse=True)
    idx = 0
    while True:
        for k in angles:
            try:
                a = asteroids[k].pop(0)
                idx += 1
                if idx == 200:
                    return (a[0] * 100 + a[1])
            except IndexError:
                pass


def main():
    data = [ x.rstrip('\n') for x in open('input10') ]

    result = 0
    point = (0, 0)
    for j, line in enumerate(data):
        for i, cell in enumerate(line):
            if cell == '#':
                res = count_asteroids(data, i, j)
                if res > result:
                    result = res
                    point = (i, j)
    print(result)

    print(destroy_asteroids(data, point[0], point[1]))

    
if __name__ == '__main__':
    main()

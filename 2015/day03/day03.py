class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def move(self, direction):
        if direction == '^':
            self._y += 1
        elif direction == 'v':
            self._y -= 1
        elif direction == '>':
            self._x += 1
        elif direction == '<':
            self._x -= 1

    @property
    def position(self):
        return f'{self._x}:{self._y}'


def count_houses_v1(data):
    houses = set()
    pos = Position(0, 0)
    houses.add(pos.position)
    for d in data:
        pos.move(d)
        houses.add(pos.position)
    return len(houses)


def count_houses_v2(data):
    houses = set()
    posS = Position(0, 0)
    posR = Position(0, 0)
    houses.add(posS.position)
    for i in range(0, len(data)-1, 2):
        posS.move(data[i])
        houses.add(posS.position)
        posR.move(data[i+1])
        houses.add(posR.position)
    return len(houses)


def main():
    with open('./input.txt') as fi:
        data = fi.readline()
        res1 = count_houses_v1(data)
        print(res1)
        res2 = count_houses_v2(data)
        print(res2)


if __name__ == "__main__":
    main()

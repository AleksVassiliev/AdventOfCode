class Map:
    def __init__(self, pattern):
        self._pattern = pattern
        self._x = 0
        self._y = 0
        self._width = len(self._pattern[0])
        self._height = len(self._pattern)

    def _step(self, x, y):
        self._x += x
        self._y += y
        if self._x >= self._width:
            self._x -= self._width
        if self._y >= self._height:
            return None
        return self._pattern[self._y][self._x]

    def path(self, x, y):
        trees = 0
        while True:
            cell = self._step(x, y)
            if cell is None:
                return trees
            if cell == '#':
                trees += 1


def make_path(pattern, x, y):
    m = Map(pattern)
    return m.path(x, y)


def count_slopes(pattern):
    result = 1
    result *= make_path(pattern, 1, 1)
    result *= make_path(pattern, 3, 1)
    result *= make_path(pattern, 5, 1)
    result *= make_path(pattern, 7, 1)
    result *= make_path(pattern, 1, 2)
    return result    


def main():
    pattern = [line.strip() for line in open('./input03.txt')]
    result_v1 = make_path(pattern, 3, 1)
    print(result_v1)
    result_v2 = count_slopes(pattern)
    print(result_v2)


if __name__ == '__main__':
    main()

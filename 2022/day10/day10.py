class CPU:
    def __init__(self):
        self._x = 1
        self._cycles = []

    def execute(self, data):
        for line in data:
            if line == 'noop':
                self._cycles.append(self._x)
            else:
                value = line.split(' ')[1]
                self._cycles.append(self._x)
                self._cycles.append(self._x)
                self._x += int(value)
        return self._cycles

    @property
    def x(self):
        return self._x

    @property
    def strength(self):
        res = 0
        for idx in [20, 60, 100, 140, 180, 220]:
            res += idx * self._cycles[idx-1]
        return res


class CRT:
    def __init__(self):
        self._image = []
        for _ in range(6):
            row = ['.' for _ in range(40)]
            self._image.append(row)

    def draw(self, data):
        x = 0
        y = 0
        for value in data:
            sprite = [value - 1, value, value + 1]
            if x in sprite:
                self._image[y][x] = '#'
            x += 1
            if x % 40 == 0:
                y += 1
                x = 0


    @property
    def image(self):
        res = []
        for row in self._image:
            res.append(''.join(row))
        return res

def calculate_x(data):
    cpu = CPU()
    cpu.execute(data)
    return cpu.x


def calculate_strength(data):
    cpu = CPU()
    cpu.execute(data)
    return cpu.strength


def draw_image(data):
    cpu = CPU()
    cycles = cpu.execute(data)
    crt = CRT()
    crt.draw(cycles)
    return crt.image


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = calculate_strength(data)
    print(result_v1)
    result_v2 = draw_image(data)
    for row in result_v2:
        print(row)


if __name__ == '__main__':
    main()

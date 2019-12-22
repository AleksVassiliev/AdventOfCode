import math
import itertools


class utils:
    @staticmethod
    def period(seq):
        l = len(seq) // 2
        for i in range(l):
            if seq[i] != seq[i+l]:
                return 0
        return l

    @staticmethod
    def gcd(seq):
        a = seq[0]
        for b in seq[1:]:
            a = (a * b) // math.gcd(a, b)
        return a


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        repr_str = '<x={}, y={}, z={}>'.format(self.x, self.y, self.z)
        return repr_str

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __eq__(self, other):
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.z != other.z:
            return False
        return True

    def value(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Moon:
    def __init__(self, x, y, z):
        self.position = Vector(x, y, z)
        self.velocity = Vector(0, 0, 0)
        self.history = [ [ x ], [ y ], [ z ] ]
        self.period = [0, 0, 0]

    def __str__(self):
        repr_str = 'position={}, velocity={}'.format(self.position, self.velocity)
        return repr_str

    def change_velocity(self, v):
        self.velocity += v

    def change_position(self):
        self.position += self.velocity
        if self.period[0] == 0:
            self.history[0].append(self.position.x)
            self.period[0] = utils.period(self.history[0])
        if self.period[1] == 0:
            self.history[1].append(self.position.y)
            self.period[1] = utils.period(self.history[1])
        if self.period[2] == 0:
            self.history[2].append(self.position.z)
            self.period[2] = utils.period(self.history[2])

    def energy(self):
        return self.position.value() * self.velocity.value()

    def is_initial(self):
        if 0 in self.period:
            return False
        return True

    def mperiod(self):
        return utils.gcd(self.period)


class MoonSystem:
    def __init__(self, data):
        self.moons = []
        for line in data:
            self.moons.append(self.parse(line))

    def __str__(self):
        repr_str = []
        for m in self.moons:
            repr_str.append('{}'.format(m))
        return '\n'.join(repr_str)

    def parse(self, line):
        values = line[1:-1].split(', ')
        x = int(values[0][2:])
        y = int(values[1][2:])
        z = int(values[2][2:])
        return Moon(x, y, z)

    def simulate(self):
        comb = itertools.combinations(self.moons, 2)
        for c in comb:
            v0, v1 = self.calculate_velocity(c[0], c[1])
            c[0].change_velocity(v0)
            c[1].change_velocity(v1)
        for idx, m in enumerate(self.moons):
            m.change_position()

    def velocity(self, value1, value2):
        if value1 == value2:
            return 0, 0
        if value1 > value2:
            return -1, 1
        if value1 < value2:
            return 1, -1

    def calculate_velocity(self, moon1, moon2):
        x1, x2 = self.velocity(moon1.position.x, moon2.position.x)
        y1, y2 = self.velocity(moon1.position.y, moon2.position.y)
        z1, z2 = self.velocity(moon1.position.z, moon2.position.z)
        return Vector(x1, y1, z1), Vector(x2, y2, z2)

    def energy(self):
        res = 0
        for m in self.moons:
            res += m.energy()
        return res

    def is_initial(self):
        res = True
        for m in self.moons:
            res = res and m.is_initial()
        return res

    def period(self):
        p = []
        for m in self.moons:
            p.append(m.mperiod())
        return utils.gcd(p)


def part1(data):
    s = MoonSystem(data)
    for i in range(1000):
        s.simulate()
    return s.energy()


def part2(data):
    s = MoonSystem(data)
    while s.is_initial() == False:
        s.simulate()
    return s.period()


def main():
    data = [ x.rstrip('\n') for x in open('input12') ]
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()

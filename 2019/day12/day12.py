import itertools


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

    def value(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


class Moon:
    def __init__(self, x, y, z):
        self.position = Vector(x, y, z)
        self.velocity = Vector(0, 0, 0)

    def __str__(self):
        repr_str = 'position={}, velocity={}'.format(self.position, self.velocity)
        return repr_str

    def change_velocity(self, v):
        self.velocity += v

    def change_position(self):
        self.position += self.velocity

    def energy(self):
        return self.position.value() * self.velocity.value()


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
        for m in self.moons:
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


def main():
    data = [ x.rstrip('\n') for x in open('input12') ]

    s = MoonSystem(data)
    for i in range(1000):
        s.simulate()
    print(s.energy())

if __name__ == '__main__':
    main()

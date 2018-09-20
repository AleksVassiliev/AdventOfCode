import collections


class Vector:
    def __init__(self, values):
        self.x = int(values[0])
        self.y = int(values[1])
        self.z = int(values[2])


    def distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)


    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        return self


    def __iadd__(self, other):
        return self.__add__(other)



class Particle:
    def __init__(self, idx, data):
        p, v, a = data.split(", ")
        self.P = Vector(p[3:-1].split(","))
        self.V = Vector(v[3:-1].split(","))
        self.A = Vector(a[3:-1].split(","))
        self.index = idx


    def tick(self):
        self.V += self.A
        self.P += self.V


    def position(self):
        return "{}.{}.{}".format(self.P.x, self.P.y, self.P.z)



class Particles:
    def __init__(self, data):
        self.data = {}
        for idx, item in enumerate(data):
            self.data[idx] = Particle(idx, item)
        self.collisions()


    def tick(self):
        for key in self.data:
            self.data[key].tick()
        self.collisions()


    def collisions(self):
        d = collections.defaultdict(list)
        for key in self.data:
            d[self.data[key].position()].append(key)

        for k in d:
            if len(d[k]) > 1:
                for i in d[k]:
                    self.data.pop(i, None)


    def size(self):
        return len(self.data)


    def __repr__(self):
        return self.data.__repr__()



def analyze(data):
    A = []
    minA = None
    for idx, item in enumerate(data):
        p, v, a = item.split(", ")
        va = Vector(a[3:-1].split(","))
        
        m = va.distance()
        if m == minA:
            A.append(idx)
        elif minA == None:
            minA = m
            A.append(idx)
        elif m < minA:
            A = []
            A.append(idx)
            minA = m
    return A


def collide(data):
    particles = Particles(data)
    for i in range(400):
        particles.tick()
    return particles.size()


def main():
    data = [ line.rstrip("\n") for line in open('input20') ]

    print(analyze(data))
    print(collide(data))



if __name__ == "__main__":
    main()

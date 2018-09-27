import copy


def test_partA():
    grid = [ "..#", "#..", "..." ]

    g = Grid(grid)
    for i in range(0, 7):
        g.burst()
    assert(g.counter == 5)

    for i in range(7, 70):
        g.burst()
    assert(g.counter == 41)

    for i in range(70, 10000):
        g.burst()
    assert(g.counter == 5587)


def test_partB():
    grid = [ "..#", "#..", "..." ]

    g = Grid(grid)
    for i in range(0, 100):
        g.burst2()
    assert(g.counter == 26)

    for i in range(100, 10000000):
        g.burst2()
    assert(g.counter == 2511944)


class Grid:
    def __init__(self, grid):
        self.infected = self.initialState(grid)
        self.flagged = []
        self.weakened = []
        self.direction = (0, 1)
        self.position = [0, 0]
        self.counter = 0
        self.cells = self.initialState2(grid)


    def initialState(self, grid):
        size = int(len(grid)/2)
        infected = []

        for row, line in enumerate(grid):
            for col, c in enumerate(line):
                if c == "#":
                    x = -(size - col)
                    y = size - row
                    infected.append("{}.{}".format(x, y))
        return infected


    def initialState2(self, grid):
        size = int(len(grid)/2)
        infected = {}

        for row, line in enumerate(grid):
            for col, c in enumerate(line):
                if c == "#":
                    x = -(size - col)
                    y = size - row
                    infected["{}.{}".format(x, y)] = "#"
        return infected


    def burst(self):
        pos = "{}.{}".format(self.position[0], self.position[1])
        if pos in self.infected:      # current node infected
            self.turnRight()
            self.infected.remove(pos)
        else:
            self.turnLeft()
            self.infected.append(pos)
            self.counter += 1
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]


    def burst2(self):
        pos = "{}.{}".format(self.position[0], self.position[1])
        if pos in self.cells:
            if self.cells[pos] == "#":
                self.turnRight()
                self.cells[pos] = "F"
            elif self.cells[pos] == "F":
                self.reverse()
                self.cells.pop(pos)
            elif self.cells[pos] == "W":
                self.cells[pos] = "#"
                self.counter += 1
        else:
            self.turnLeft()
            self.cells[pos] = "W"
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]


    def turnLeft(self):
        if self.direction == (0, 1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, 1)


    def turnRight(self):
        if self.direction == (0, 1):
            self.direction = (1, 0)
        elif self.direction == (1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, 1)


    def reverse(self):
        self.direction = (self.direction[0] * (-1), self.direction[1] * (-1))



def main():
    grid = [ line.rstrip("\n") for line in open("input22") ]

    gA = Grid(grid)
    for i in range(10000):
        gA.burst()
    print(gA.counter)


    gB = Grid(grid)
    for i in range(10000000):
        gB.burst2()
    print(gB.counter)


if __name__ == "__main__":
    main()

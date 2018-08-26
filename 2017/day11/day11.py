def test_partA():
    assert(stepsCount("ne,ne,ne") == 3)
    assert(stepsCount("ne,ne,sw,sw") == 0)
    assert(stepsCount("ne,ne,s,s") == 2)
    assert(stepsCount("se,sw,se,sw,sw") == 3)


def stepsCount(path):
    steps = path.split(",")
    grid = HexGrid()
    grid.path(steps)
    return grid.distance()



movement = { "n":  [  1, -1,  0 ],
             "ne": [  1,  0, -1 ],
             "se": [  0,  1, -1 ],
             "s":  [ -1,  1,  0 ],
             "sw": [ -1,  0,  1 ],
             "nw": [  0, -1,  1 ]      
           }


class HexCell:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


    def move(self, direction):
        step = movement[direction]
        self.x += step[0]
        self.y += step[1]
        self.z += step[2]


    def distance(self):
        return abs(max([self.x, self.y, self.z], key=abs))


class HexGrid:
    def __init__(self):
        self.position = HexCell()
        self.maxDistance = 0


    def path(self, steps):
        for step in steps:
            self.move(step)        


    def move(self, direction):
        self.position.move(direction)
        self.maxDistance = max(self.maxDistance, self.position.distance())


    def distance(self):
        return self.position.distance()



def main():
    with open("input11", "r") as f:
        steps = f.read().rstrip("\n").split(",")
        grid = HexGrid()
        grid.path(steps)
        print(grid.distance())
        print(grid.maxDistance)



if __name__ == "__main__":
    main()

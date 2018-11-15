class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == '^':
            self.moveN()
        elif direction == 'v':
            self.moveS()
        elif direction == '>':
            self.moveE()
        elif direction == '<':
            self.moveW()

    def moveN(self):
        self.y += 1

    def moveS(self):
        self.y -= 1

    def moveW(self):
        self.x -= 1
    
    def moveE(self):
        self.x += 1

    def pos(self):
        return "{}:{}".format(self.x, self.y)


def calculateA(data):
    houses = set()
    pos = Position(0, 0)
    houses.add(pos.pos())
    for d in data:
        pos.move(d)
        houses.add(pos.pos())
    return len(houses)


def calculateB(data):
    houses = set()
    posS = Position(0, 0)
    posR = Position(0, 0)
    houses.add(posS.pos())
    for idx, d in enumerate(data):
        if idx % 2 == 0:
            posS.move(d)
            houses.add(posS.pos())
        else:
            posR.move(d)
            houses.add(posR.pos())
    return len(houses)


def main():
    with open("input03") as f:
        data = f.read()
        res1 = calculateA(data)
        res2 = calculateB(data)
        print(res1, res2)


if __name__ == "__main__":
    main()

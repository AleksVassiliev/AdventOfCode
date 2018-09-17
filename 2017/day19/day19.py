def test_partA():
    diagram = [ "     |          ",
                "     |  +--+    ",
                "     A  |  C    ",
                " F---|----E|--+ ",
                "     |  |  |  D ",
                "     +B-+  +--+ ",
                "                "
              ]

    assert(routeA(diagram) == "ABCDEF")
    assert(routeB(diagram) == 38)


def test_partB():
    diagram = [ "     |          ",
                "     |  +--+    ",
                "     A  |  C    ",
                " F---|----E|--+ ",
                "     |  |  |  D ",
                "     +B-+  +--+ ",
                "                "
              ]

    assert(routeB(diagram) == 38)



class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def __str__(self):
        return "[ {}, {} ]".format(self.x, self.y)


class RoutingDiagram:
    def __init__(self, diagram):
        self.diagram = []
        for line in diagram:
            self.diagram.append(list(line))

        self.current = self.findEntrance()
        self.rows = len(self.diagram)
        self.cols = len(self.diagram[0])

        self.steps = 0


    def findEntrance(self):
        for idx, cell in enumerate(self.diagram[0]):
            if cell == "|":
                return Coord(idx, 0)


    def route(self):
        direction = Coord(0, 1)
        route = []
        value = self.cell(self.current.x, self.current.y)
        while value != None:
            value = self.cell(self.current.x, self.current.y)
            if value == None:
                return "".join(route)
            elif value == "-":
                self.steps += 1
            elif value == "|":
                self.steps += 1
            elif value == " ":
                return "".join(route)
            elif value == "+":
                self.steps += 1
                if direction.x == 0:
                    c = self.cell(self.current.x - 1, self.current.y)
                    if  (c == "-") or (c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        direction.x = -1
                        direction.y = 0
                    else:
                        direction.x = 1
                        direction.y = 0
                elif direction.y == 0:
                    c = self.cell(self.current.x, self.current.y - 1)
                    if (c == "|") or (c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                        direction.x = 0
                        direction.y = -1
                    else:
                        direction.x = 0
                        direction.y = 1
            else:
                self.steps += 1
                route.append(value)

            self.current += direction



    def cell(self, x, y):
        if (0 <= y < self.rows) and (0 <= x < self.cols):
            return self.diagram[y][x]
        return None



def routeA(diagram):
    rd = RoutingDiagram(diagram)
    res = rd.route()
    return res


def routeB(diagram):
    rd = RoutingDiagram(diagram)
    res = rd.route()
    return rd.steps



def main():
    diagram = [ line.rstrip('\n') for line in open('input19') ]
    print(routeA(diagram))
    print(routeB(diagram))


if __name__ == "__main__":
    main()

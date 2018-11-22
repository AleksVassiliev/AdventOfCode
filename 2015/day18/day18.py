class Grid:
    def __init__(self, grid):
        self.grid = []
        self.gridnext = []
        for line in grid:
            gridline = []
            for c in line:
                gridline.append(c)
            self.grid.append(gridline.copy())
            self.gridnext.append(gridline.copy())

        self.width = len(self.grid[0])
        self.height = len(self.grid)


    def turnOn(self, x, y):
        self.grid[y][x] = '#'


    def turnOff(self, x, y):
        self.grid[y][x] = '.'


    def isOn(self, x, y):
        return self.grid[y][x] == '#'


    def checkOn(self, x, y):
        if x < 0:
            return False
        if x >= self.width:
            return False
        if y < 0:
            return False
        if y >= self.height:
            return False
        return self.isOn(x, y)


    def isOff(self, x, y):
        return self.grid[y][x] == '.'


    def getState(self, x, y):
        return self.grid[y][x]


    def updateGrid(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = self.gridnext[y][x]


    def countLights(self):
        res = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.isOn(x, y):
                    res += 1
        return res


    def neighbors(self, x, y):
        res = 0
        coord = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
        for c in coord:
            if self.checkOn(x+c[0], y+c[1]) == True:
                res += 1
        return res


    def updateLights(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                n = self.neighbors(x, y)
                if self.isOn(x, y):
                    if (n == 2) or (n == 3):
                        pass
                    else:
                        self.gridnext[y][x] = '.'
                else:
                    if n == 3:
                        self.gridnext[y][x] = '#'
        self.updateGrid()


    def updateCorners(self):
        self.turnOn(0, 0)
        self.turnOn(0, self.height-1)
        self.turnOn(self.width-1, 0)
        self.turnOn(self.width-1, self.height-1)



def main():
    grid = [ line.rstrip("\n") for line in open("input18") ]

    g = Grid(grid)
    for i in range(100):
        g.updateLights()
    print(g.countLights())

    g = Grid(grid)
    g.updateCorners()
    for i in range(100):
        g.updateLights()
        g.updateCorners()
    print(g.countLights())



if __name__ == "__main__":
    main()

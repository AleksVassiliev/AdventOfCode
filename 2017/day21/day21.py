def test_partA():
    patterns = [ "../.# => ##./#../...",
                 ".#./..#/### => #..#/..../..../#..#"
               ]

    g = Grid()
    g.setPatterns(patterns)

    g.enchance()
    g.enchance()
    
    assert(g.weight() == 12)



class Grid:
    def __init__(self):
        self.size = 3
        self.grid = [ [ '.', '#', '.' ], [ '.', '.', '#' ], [ '#', '#', '#' ] ]


    def __repr__(self):
        line = "\n"
        for row in self.grid:
            r = "".join(row)
            l = "{}\n".format(r)
            line += l
        return line


    def setPatterns(self, patterns):
        self.patterns2 = {}
        self.patterns3 = {}
        for p in patterns:
            a, b = p.split(" => ")
            if len(a) == 5:
                self.patterns2[a] = b
            elif len(a) == 11:
                self.patterns3[a] = b


    def weight(self):
        w = 0
        for row in range(0, self.size):
            for col in range(0, self.size):
                if self.grid[row][col] == "#":
                    w += 1
        return w


    def enchance(self):
        if self.size % 2 == 0:
            self.enchance2()
        elif self.size % 3 == 0:
            self.enchance3()


    def getPattern2(self, p):
        if p in self.patterns2:
            return self.patterns2[p]

        flipH = "{}{}/{}{}".format(p[3], p[4], p[0], p[1])
        if flipH in self.patterns2:
            return self.patterns2[flipH]

        flipV = "{}{}/{}{}".format(p[1], p[0], p[4], p[3])
        if flipV in self.patterns2:
            return self.patterns2[flipV]

        rot90 = "{}{}/{}{}".format(p[3], p[0], p[4], p[1])
        if rot90 in self.patterns2:
            return self.patterns2[rot90]

        rot90flipH = "{}{}/{}{}".format(p[4], p[1], p[3], p[0])
        if rot90flipH in self.patterns2:
            return self.patterns2[rot90flipH]

        rot90flipV = "{}{}/{}{}".format(p[0], p[3], p[1], p[4])
        if rot90flipV in self.patterns2:
            return self.patterns2[rot90flipV]

        rot180 = "{}{}/{}{}".format(p[4], p[3], p[1], p[0])
        if rot180 in self.patterns2:
            return self.patterns2[rot180]

        rot270 = "{}{}/{}{}".format(p[1], p[4], p[0], p[3])
        if rot270 in self.patterns2:
            return self.patterns2[rot270]

        return "***/***/***"


    def getPattern3(self, p):
        if p in self.patterns3:
            return self.patterns3[p]

        flipH = "{}{}{}/{}{}{}/{}{}{}".format(p[8], p[9], p[10], p[4], p[5], p[6], p[0], p[1], p[2])
        if flipH in self.patterns3:
            return self.patterns3[flipH]

        flipV = "{}{}{}/{}{}{}/{}{}{}".format(p[2], p[1], p[0], p[6], p[5], p[4], p[10], p[9], p[8])
        if flipV in self.patterns3:
            return self.patterns3[flipV]

        rot90 = "{}{}{}/{}{}{}/{}{}{}".format(p[8], p[4], p[0], p[9], p[5], p[1], p[10], p[6], p[2])
        if rot90 in self.patterns3:
            return self.patterns3[rot90]

        rot90flipH = "{}{}{}/{}{}{}/{}{}{}".format(p[10], p[6], p[2], p[9], p[5], p[1], p[8], p[4], p[0])
        if rot90flipH in self.patterns3:
            return self.patterns3[rot90flipH]

        rot180 = "{}{}{}/{}{}{}/{}{}{}".format(p[10], p[9], p[8], p[6], p[5], p[4], p[2], p[1], p[0])
        if rot180 in self.patterns3:
            return self.patterns3[rot180]

        rot270 = "{}{}{}/{}{}{}/{}{}{}".format(p[2], p[6], p[10], p[1], p[5], p[9], p[0], p[4], p[8])
        if rot270 in self.patterns3:
            return self.patterns3[rot270]

        rot270flipH = "{}{}{}/{}{}{}/{}{}{}".format(p[0], p[4], p[8], p[1], p[5], p[9], p[2], p[6], p[10])
        if rot270flipH in self.patterns3:
            return self.patterns3[rot270flipH]

        return "****/****/****/****"



    def enchance2(self):
        self.newsize = int(self.size / 2 * 3)
        self.newgrid = [ [ ' ' for x in range (0, self.newsize)] for y in range(0, self.newsize) ]

        for row in range(0, self.size, 2):
            for col in range(0, self.size, 2):
                grid = ""
                grid += "".join(self.grid[row][col:col+2]) + "/"
                grid += "".join(self.grid[row+1][col:col+2])

                lines = self.getPattern2(grid).split("/")
                newrow = int(row/2 * 3)
                for l in lines:
                    newcol = int(col/2 * 3)
                    for c in l:
                        self.newgrid[newrow][newcol] = c
                        newcol += 1
                    newrow += 1

        self.grid = self.newgrid
        self.size = self.newsize



    def enchance3(self):
        self.newsize = int(self.size / 3 * 4)
        self.newgrid = [ [ ' ' for x in range (0, self.newsize)] for y in range(0, self.newsize) ]

        for row in range(0, self.size, 3):
            for col in range(0, self.size, 3):
                grid = ""
                grid += "".join(self.grid[row][col:col+3]) + "/"
                grid += "".join(self.grid[row+1][col:col+3]) + "/"
                grid += "".join(self.grid[row+2][col:col+3])

                lines = self.getPattern3(grid).split("/")
                newrow = int(row/3 * 4)
                for l in lines:
                    newcol = int(col/3 * 4)
                    for c in l:
                        self.newgrid[newrow][newcol] = c
                        newcol += 1
                    newrow += 1

        self.grid = self.newgrid
        self.size = self.newsize




def main():
    patterns = [ line.rstrip("\n") for line in open("input21") ]

    g = Grid()
    g.setPatterns(patterns)

    for i in range(5):
        g.enchance()

    print(g.weight())

    for i in range(5, 18):
        g.enchance()

    print(g.weight())



if __name__ == "__main__":
    main()

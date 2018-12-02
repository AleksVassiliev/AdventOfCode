class Grid:
    def __init__(self):
        self.width = 50
        self.height = 6
        self.grid = [] * self.height
        for i in range(self.height):
            self.grid.append(["."] * self.width)


    def execute(self, program):
        for line in program:
            instr = line.split()
            if instr[0] == "rect":
                self.cmd_rect(instr[1])
            elif instr[0] == "rotate":
                if instr[1] == "column":
                    col = int(instr[2][2:])
                    value = int(instr[4])
                    self.cmd_rotate_column(col, value)
                elif instr[1] == "row":
                    row = int(instr[2][2:])
                    value = int(instr[4])
                    self.cmd_rotate_row(row, value)


    def cmd_rect(self, dim):
        x, y = map(int, dim.split("x"))
        for c in range(y):
            for r in range(x):
                self.grid[c][r] = "#"


    def cmd_rotate_column(self, col, value):
        orig = [ self.grid[r][col] for r in range(self.height) ]
        value = (self.height - value)
        shifted = orig[value:] + orig[:value]
        for idx, val in enumerate(shifted):
            self.grid[idx][col] = val


    def cmd_rotate_row(self, row, value):
        value = (self.width - value)
        self.grid[row] = self.grid[row][value:] + self.grid[row][:value]


    def pixels(self):
        res = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == "#":
                    res += 1
        return res


    def dump(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.grid[y][x]
            print(line)


def main():
    program = [ line.rstrip("\n") for line in open("input08") ]

    g = Grid()
    g.execute(program)
    g.dump()
    print(g.pixels())


if __name__ == "__main__":
    main()

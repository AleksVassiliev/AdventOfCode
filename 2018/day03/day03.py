import re


class Grid:
    def __init__(self):
        self.grid = []
        self.width = 1000
        self.height = 1000
        for i in range(self.height):
            self.grid.append(['.'] * self.width)


    def fillGrid(self, cid, left, top, width, height):
        for r in range(height):
            for c in range(width):
                try:
                    if self.grid[r+top][c+left] == '.':
                        self.grid[r+top][c+left] = set()
                        self.grid[r+top][c+left].add(cid)
                    else:
                        self.grid[r+top][c+left].add(cid)
                except IndexError as e:
                    print("ERROR: {} x {}".format(r+top, c+left))
                    raise e


    def overlaps(self):
        res = 0
        cid_all = set()
        cid_over = set()
        for y in range(self.height):
            for x in range(self.width):
                if type(self.grid[y][x]) == set:
                    if len(self.grid[y][x]) > 1:
                        res += 1
                        cid_over.update(self.grid[y][x])
                    else:
                        cid_all.update(self.grid[y][x])
        return res, cid_all.difference(cid_over)
        


def parse_line(text):
    regexp = "#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)"
    res = re.search(regexp, text)
    return map(int, res.groups())



def main():
    data = [ line.rstrip("\n") for line in open("input03") ]    

    g = Grid()
    for item in data:
        cid, left, top, width, height = parse_line(item)
        g.fillGrid(cid, left, top, width, height)
    print(g.overlaps())


if __name__ == "__main__":
    main()

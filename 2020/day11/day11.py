class Layout:
    def __init__(self, data, v2=False):
        self.layout = []
        for line in data:
            self.layout.append(list(line))
        self.width = len(self.layout[0])
        self.height = len(self.layout)
        self.v2 = v2
        self.max_occupied = 5 if self.v2 else 4


    def state(self, x, y):
        if self.layout[y][x] == '.':
            return '.'
        coord = [(-1,1), (0,1), (1,1), (-1,0), (1,0), (-1,-1), (0,-1), (1,-1)]
        if not self.v2:
            res = sum(self.calculate_state_v1(x + c[0], y + c[1]) for c in coord)
        else:
            res = sum(self.calculate_state_v2(x, y, c[0], c[1]) for c in coord)
        if self.layout[y][x] == 'L' and res == 0:
            return '#'
        if self.layout[y][x] == '#' and res >= self.max_occupied:
            return 'L'
        return self.layout[y][x]

    def calculate_state_v1(self, x, y):
        if (0 <= x < self.width) and (0 <= y < self.height):
            return self.layout[y][x] == '#' 
        return False

    def calculate_state_v2(self, x, y, diff_x, diff_y):
        while True:
            x += diff_x
            y += diff_y
            if (0 <= x < self.width) and (0 <= y < self.height):
                if self.layout[y][x] != '.':
                    return self.layout[y][x] == '#'
            else:
                return False
  
    def __str__(self):
        lines = []
        for line in self.layout:
            newline = ''
            for c in line:
                newline += c
            lines.append(newline)
        return '\n'.join(lines)

    def occupied_seats(self):
        res = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.layout[y][x] == '#':
                    res += 1
        return res

    def __eq__(self, other):
        for row in range(self.height):
            for col in range(self.width):
                if self.layout[row][col] != other.layout[row][col]:
                    return False
        return True


def calculate_seats(layout, v2=False):
    cur = Layout(layout, v2)
    while True:
        next_layout = Layout(layout, v2)
        for y in range(cur.height):
            for x in range(cur.width):
                next_layout.layout[y][x] = cur.state(x, y)
        if cur == next_layout:
            break
        cur = next_layout
    return next_layout.occupied_seats()


def main():
    layout = [line.strip() for line in open('./input11.txt')]
    result_v1 = calculate_seats(layout)
    print(result_v1)
    result_v2 = calculate_seats(layout, True)
    print(result_v2)


if __name__ == '__main__':
    main()

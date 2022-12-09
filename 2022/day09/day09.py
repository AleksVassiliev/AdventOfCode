class Rope:
    class Knot:
        def __init__(self):
            self.x = 0
            self.y = 0

        @property
        def position(self):
            return f'{self.x}:{self.y}'


    def __init__(self, sz):
        self._rope = [Rope.Knot() for _ in range(sz)]
        self._tpos = set()
        self._tpos.add(self.position)

    def move(self, direction, steps):
        for _ in range(int(steps)):
            if direction == 'U':
                self._rope[0].y += 1
            elif direction == 'D':
                self._rope[0].y -= 1
            elif direction == 'R':
                self._rope[0].x += 1
            elif direction == 'L':
                self._rope[0].x -= 1
            self.update_rope()

    def update_rope(self):
        for i in range(len(self._rope) - 1):
            hx, hy = self._rope[i].x, self._rope[i].y 
            tx, ty = self._rope[i+1].x, self._rope[i+1].y
            if hy == ty:            # same row
                if (hx - tx) > 1:
                    self._rope[i+1].x += 1
                elif (tx - hx) > 1:
                    self._rope[i+1].x -= 1
            elif hx == tx:          # same column
                if (hy - ty) > 1:
                    self._rope[i+1].y += 1
                elif (ty - hy) > 1:
                    self._rope[i+1].y -= 1
            else:                   # diagonal
                if not ((hx - 1 <= tx <= hx + 1) and ((hy - 1 <= ty <= hy + 1))):
                    if hx > tx:
                        self._rope[i+1].x += 1
                    elif tx > hx:
                        self._rope[i+1].x -= 1
                    if hy > ty:
                        self._rope[i+1].y += 1
                    elif ty > hy:
                        self._rope[i+1].y -= 1
            self._tpos.add(self.position)

    @property
    def position(self):
        return self._rope[-1].position


def count_positions_v1(moves):
    rope = Rope(2)
    for line in moves:
        dir, cnt = line.split(' ')
        rope.move(dir, cnt)
    return len(rope._tpos)


def count_positions_v2(moves):
    rope = Rope(10)
    for line in moves:
        dir, cnt = line.split(' ')
        rope.move(dir, cnt)
    return len(rope._tpos)


def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = count_positions_v1(data)
    print(result_v1)
    result_v2 = count_positions_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

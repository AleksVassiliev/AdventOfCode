class Board:
    def __init__(self):
        self._board = []
        self._finished = False

    @property
    def score(self):
        res = 0
        for row in self._board:
            for item in row:
                if item:
                    res += item
        return res

    @property
    def is_finished(self):
        return self._finished

    def add_row(self, row):
        self._board.append(row)

    def pass_number(self, num):
        for row in self._board:
            if num in row:
                col_idx = row.index(num)
                row[col_idx] = None
                if not any(row):
                    self._finished = True
                    return True
                for row_idx in range(0, len(self._board)):
                    if self._board[row_idx][col_idx] is not None:
                        return False
                self._finished = True
                return True
        return False


def parse_data(data):
    numbers = [int(x) for x in data[0].split(',')]
    boards = []
    board = Board()
    for line in data[2:]:
        if line == '':
            boards.append(board)
            board = Board()
        else:
            cells = [int(x) for x in line.split()]
            board.add_row(cells)
    boards.append(board)
    return numbers, boards


def calculate_score_v1(data):
    numbers, boards = parse_data(data)
    for num in numbers:
        for board in boards:
            res = board.pass_number(num)
            if res:
                return num * board.score


def calculate_score_v2(data):
    numbers, boards = parse_data(data)
    score = 0
    for num in numbers:
        boards_new = []
        for board in boards:
            if not board.is_finished:
                boards_new.append(board)
        if not boards_new:
            return score
        for board in boards_new:
            res = board.pass_number(num)
            if res:
                score = num * board.score


def main():
    data = [line.strip() for line in open('./input04.txt')]
    result_v1 = calculate_score_v1(data)
    print(result_v1)
    result_v2 = calculate_score_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

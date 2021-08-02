def calculate_seat(seat_str):
    row_str = seat_str[:-3]
    col_str = seat_str[-3:]
    row = (0, 127)
    for ch in row_str:
        if ch == 'B':
            row = (int((row[0] + row[1])/2) + 1, row[1])
        elif ch == 'F':
            row = (row[0], int((row[0] + row[1])/2))
    col = (0, 7)
    for ch in col_str:
        if ch == 'R':
            col = (int((col[0] + col[1])/2) + 1, col[1])
        elif ch == 'L':
            col = (col[0], int((col[0] + col[1])/2))
    return (row[0], col[0], row[0] * 8 + col[0])


def find_highest_seat(seats):
    seat_id = 0
    for seat in seats:
        seat_id = max(seat_id, calculate_seat(seat)[2])
    return seat_id


def find_seat(seats):
    seat_ids = []
    for seat in seats:
        seat_ids.append(calculate_seat(seat)[2])
    seat_ids.sort()
    seat_id = seat_ids[0]
    for item in seat_ids:
        if seat_id != item:
            return seat_id
        seat_id += 1


def main():
    data = [line.strip() for line in open('./input05.txt')]
    result_v1 = find_highest_seat(data)
    print(result_v1)
    result_v2 = find_seat(data)
    print(result_v2)


if __name__ == '__main__':
    main()

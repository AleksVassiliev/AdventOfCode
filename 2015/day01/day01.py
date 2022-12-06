def solve_v1(data):
    res = 0
    for c in data:
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
    return res


def solve_v2(data):
    res = 0
    for idx, c in enumerate(data):
        if c == '(':
            res += 1
        elif c == ')':
            res -= 1
        if res == -1:
            return (idx + 1)
    return 0


def main():
    with open("input.txt", "r") as f:
        data = f.read()
        res1 = solve_v1(data)
        print(res1)
        res2 = solve_v2(data)
        print(res2)


if __name__ == "__main__":
    main()

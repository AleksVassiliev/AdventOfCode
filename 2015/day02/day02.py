def calculate_papper(data):
    (l, w, h) = [int(x) for x in data.split('x')]
    lw = l * w
    wh = w * h
    hl = h * l
    return (2 * (lw + wh + hl) + min(lw, wh, hl))


def calculate_v1(data):
    res = 0
    for item in data:
        res += calculate_papper(item)
    return res


def calculate_ribbon(data):
    (l, w, h) = [int(x) for x in data.split('x')]
    return (2 * (l + w + h - max(l, w, h)) + (l * w * h))


def calculate_v2(data):
    res = 0
    for item in data:
        res += calculate_ribbon(item)
    return res


def main():
    data = [ line.rstrip('\n') for line in open('input.txt') ]
    res1 = calculate_v1(data)
    print(res1)
    res2 = calculate_v2(data)
    print(res2)


if __name__ == "__main__":
    main()

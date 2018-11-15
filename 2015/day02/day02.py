def calculateA(data):
    res = 0
    for item in data:
        l, w, h = item.split('x')
        lw = int(l) * int(w)
        wh = int(w) * int(h)
        hl = int(h) * int(l)
        res += 2 * (lw + wh + hl) + min(lw, wh, hl)
    return res


def calculateB(data):
    res = 0
    for item in data:
        l, w, h = item.split('x')
        l = int(l)
        w = int(w)
        h = int(h)
        val1 = 2 * (l + w + h - max(l, w, h))
        val2 = l * w * h
        res += (val1 + val2)
    return res


def main():
    data = [ line.rstrip("\n") for line in open("input02") ]
    res1 = calculateA(data)
    res2 = calculateB(data)
    print(res1, res2)


if __name__ == "__main__":
    main()

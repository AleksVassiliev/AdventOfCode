def truncate(text):
    text = text[1:-1]
    res = 0
    idx = 0
    while idx < len(text):
        if text[idx] == "\\":
            if text[idx+1] == "x":
                idx += 4
            else:
                idx += 2
        else:
            idx += 1
        res += 1
    return res


def encode(text):
    res = 0
    for i in range(len(text)):
        res += 1
        if text[i] == "\\" or text[i] == "\"":
            res += 1
    return (res + 2)


def calculate(text):
    length = len(text)
    memory = truncate(text)
    coded = encode(text)
    return (length, memory, coded)


def main():
    content = [ line.rstrip("\n") for line in open("input08") ]

    res1 = 0
    res2 = 0
    for line in content:
        (l, m, c) = calculate(line)
        res1 += (l - m)
        res2 += (c - l)

    print(res1, res2)


if __name__ == "__main__":
    main() 
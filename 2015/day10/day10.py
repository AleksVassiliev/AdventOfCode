def encode(value):
    res = ""
    length = len(value)
    
    char = value[0]
    count = 1
    idx = 1
    while idx < length:
        if value[idx] == char:
            count += 1
        else:
            res += "{}{}".format(count, char)
            char = value[idx]
            count = 1
        idx += 1
    res += "{}{}".format(count, char)
    return res


def main():
    value = "1113222113"

    for i in range(50):
        value = encode(value)
        if i == 39:
            print(len(value))
    print(len(value))



if __name__ == "__main__":
    main()

def test_partA():
    assert(bufferValue(3) == 638)


def bufferValue(step):
    buff = [ 0 ]
    pos = 0
    size = 1
    while size != 2018:
        pos += step
        while pos >= size:
            pos -= size
        pos += 1
        buff.insert(pos, size)
        size += 1
    return buff[pos + 1] 


def bufferValue2(step):
    value = 0
    pos = 0
    for size in range(1, 50000001):
        pos += step
        while pos >= size:
            pos -= size
        pos += 1
        if pos == 1:
            value = size
    return value


def main():
    print(bufferValue(303))
    print(bufferValue2(303))


if __name__ == "__main__":
    main()
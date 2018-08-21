def offsets(lst):
    lst = [ int(x) for x in lst]

    steps = 0
    offset = 0
    while offset < len(lst):
        ptr = lst[offset]
        lst[offset] += 1
        offset = ptr + offset
        steps += 1 
    return steps


def offsets2(lst):
    lst = [ int(x) for x in lst]

    steps = 0
    offset = 0
    while offset < len(lst):
        ptr = lst[offset]
        if ptr >= 3:
            lst[offset] -= 1
        else:
            lst[offset] += 1    
        offset = ptr + offset
        steps += 1 
    return steps


def main():
    test = [ '0', '3', '0', '1', '-3' ]
    assert(offsets(test) == 5)

    content = [ line.rstrip('\n') for line in open('input05') ]
    print(offsets(content))

    assert(offsets2(test) == 10)

    print(offsets2(content))


if __name__ == "__main__":
    main()
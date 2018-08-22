def test_partA():
    assert(countScore("{}") == 1)
    assert(countScore("{{{}}}") == 6)
    assert(countScore("{{},{}}") == 5)
    assert(countScore("{{{},{},{{}}}}") == 16)
    assert(countScore("{<a>,<a>,<a>,<a>}") == 1)
    assert(countScore("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9)
    assert(countScore("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9)
    assert(countScore("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3)


def test_partB():
    assert(countGarbage('<>') == 0)
    assert(countGarbage('<random characters>') == 17)
    assert(countGarbage('<<<<>') == 3)
    assert(countGarbage('<{!>}>') == 2)
    assert(countGarbage('<!!>') == 0)
    assert(countGarbage('<!!!>>') == 0)
    assert(countGarbage('<{o"i!a,<{i<a>') == 10)



def cleanPattern(pattern):
    res = []
    flag = True
    for c in pattern:
        if flag == False:
            flag = True
        else:
            if c == "!":
                flag = False
            else:
                res.append(c)
    return "".join(res)


def removeGarbage(pattern):
    res = []
    flag = True
    for c in pattern:
        if c == "<":
            flag = False
        elif c == ">":
            flag = True
        else:
            if flag == True:
                res.append(c)
    return "".join(res)


def countGarbage(pattern):
    pattern = cleanPattern(pattern)

    res = 0
    flag = False
    for c in pattern:
        if c == "<":
            if flag == True:
                res += 1
            flag = True
        elif c == ">":
            flag = False
        else:
            if flag == True:
                res += 1

    return res


def countScore(pattern):
    pattern = cleanPattern(pattern)
    pattern = removeGarbage(pattern)

    score = 0
    group = 0
    for c in pattern:
        if c == "{":
            group += 1
        elif c == "}":
            score += group
            group -= 1
    return score



def main():
    with open('input09', 'r') as file:
        pattern = file.read().rstrip("\n")

        print(countScore(pattern))
        print(countGarbage(pattern))


if __name__ == "__main__":
    main()

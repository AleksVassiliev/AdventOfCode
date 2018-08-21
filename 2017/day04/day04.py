def isValid(str):
    srcList = str.split(" ")
    srcSet = set(srcList)
    return (len(srcList) == len(srcSet))


def generateString(text):
    lst = [ x for x in text ]
    lst.sort()
    return "".join(lst)


def isValid2(str):
    srcList = str.split(" ")
    trgList = []
    for src in srcList:
        for trg in trgList:
            if len(src) == len(trg):
                srcStr = generateString(src)
                trgStr = generateString(trg)
                if srcStr == trgStr:
                    return False
        trgList.append(src)
    return True


def main():
    assert(isValid("aa bb cc dd ee") == True)
    assert(isValid("aa bb cc dd aa") == False)
    assert(isValid("aa bb cc dd aaa") == True)

    content = [ line.rstrip('\n') for line in open('input04') ]

    counter = 0
    for item in content:
        if isValid(item) == True:
            counter += 1
    print(counter)


    assert(isValid2("abcde fghij") == True)
    assert(isValid2("abcde xyz ecdab") == False)
    assert(isValid2("a ab abc abd abf abj") == True)
    assert(isValid2("iiii oiii ooii oooi oooo") == True)
    assert(isValid2("oiii ioii iioi iiio") == False)

    counter = 0
    for item in content:
        if isValid2(item) == True:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()

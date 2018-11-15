vowels = [ 'a', 'e', 'i', 'o', 'u' ]
strings = [ 'ab', 'cd', 'pq', 'xy' ]


def isNiceStringA(text):
    count = 0
    for v in vowels:
        count += text.count(v)
        if count >= 3:
            break
    if count < 3:
        return False

    for s in strings:
        if text.find(s) != -1:
            return False

    prev = None
    for c in text:
        if c == prev:
            return True
        else:
            prev = c

    return False


def rule1B(text):
    stringLen = len(text)
    for i in range(0, stringLen - 3):
        substr = text[i:i+2]
        if text[i+2:].find(substr) != -1:
            return True
    return False


def rule2B(text):
    stringLen = len(text)
    for i in range(0, stringLen - 2):
        substr = text[i:i+3]
        if substr[0] == substr[2]:
            return True
    return False


def isNiceStringB(text):
    if rule1B(text) == True:
        return rule2B(text)
    return False


def calculateA(data):
    res = 0
    for item in data:
        if isNiceStringA(item) == True:
            res += 1
    return res


def calculateB(data):
    res = 0
    for item in data:
        if isNiceStringB(item) == True:
            res += 1
    return res


def main():
    data = [ line.rstrip("\n") for line in open("input05") ]
    res1 = calculateA(data)
    res2 = calculateB(data)
    print(res1, res2)


if __name__ == "__main__":
    main()

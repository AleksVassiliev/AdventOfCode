def is_nice_string_v1(text):
    count = 0
    for v in ['a', 'e', 'i', 'o', 'u']:
        count += text.count(v)
        if count >= 3:
            break
    if count < 3:
        return False
    for s in ['ab', 'cd', 'pq', 'xy']:
        if text.find(s) != -1:
            return False
    prev = None
    for c in text:
        if c == prev:
            return True
        else:
            prev = c
    return False


def count_strings_v1(data):
    res = 0
    for item in data:
        if is_nice_string_v1(item) == True:
            res += 1
    return res


def is_nice_string_v2(text):
    def rule1(text):
        sz = len(text)
        for i in range(0, sz-3):
            substr = text[i:i+2]
            if text[i+2:].find(substr) != -1:
                return True
        return False

    def rule2(text):
        sz = len(text)
        for i in range(0, sz-2):
            substr = text[i:i+3]
            if substr[0] == substr[2]:
                return True
        return False         

    return (rule1(text) and rule2(text))


def count_strings_v2(data):
    res = 0
    for item in data:
        if is_nice_string_v2(item) == True:
            res += 1
    return res


def main():
    data = [line.rstrip("\n") for line in open("input.txt")]
    res1 = count_strings_v1(data)
    print(res1)
    res2 = count_strings_v2(data)
    print(res2)


if __name__ == "__main__":
    main()

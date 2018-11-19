def check1(value):
    lst = [ ord(x) for x in value ]
    for i in range(0, len(lst)-2):
        if lst[i] == lst[i+1] - 1:
            if lst[i+1] == lst[i+2] - 1:
                return True
    return False


def check2(value):
    for l in ['i', 'o', 'l']:
        for c in value:
            if c == l:
                return False
    return True 


def check3(value):
    count = set()
    letter = value[0]
    for i in range(1, len(value)):
        if letter == value[i]:
            count.add(letter)
        letter = value[i]
    if len(count) > 1:
        return True
    return False


def check_password(value):
    return check1(value) and check2(value) and check3(value)


def generate_password(text):
    res = ""
    borrow = 1
    for i in range(len(text), 0, -1):
        letter = borrow + ord(text[i-1])
        borrow = 0
        if letter > 122:
            letter = ord('a')
            borrow = 1
        res = chr(letter) + res
    return res


def next_password(passwd):
    while True:
        passwd = generate_password(passwd)
        if check_password(passwd) == True:
            return passwd


def main():
    password = "vzbxkghb"
    password = next_password(password)
    print(password)
    password = next_password(password)
    print(password)


if __name__ == "__main__":
    main()

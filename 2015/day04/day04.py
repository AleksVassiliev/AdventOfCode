import hashlib


def hash5(data):
    idx = 0
    while True:
        m = hashlib.md5()
        idx += 1
        input_string = "{}{}".format(data, idx)
        m.update(input_string.encode())
        hash_string = m.hexdigest()
        if hash_string.startswith("00000"):
            return idx


def hash6(data):
    idx = 0
    while True:
        m = hashlib.md5()
        idx += 1
        input_string = "{}{}".format(data, idx)
        m.update(input_string.encode())
        hash_string = m.hexdigest()
        if hash_string.startswith("000000"):
            return idx


def main():
    data = "bgvyzdsv"
    res1 = hash5(data)
    res2 = hash6(data)
    print(res1, res2)


if __name__ == "__main__":
    main()

import hashlib


def calculate_hash(data, prefix):
    idx = 0
    while True:
        idx += 1
        input_string = f'{data}{idx}'
        m = hashlib.md5()
        m.update(input_string.encode())
        hash_string = m.hexdigest()
        if hash_string.startswith(prefix):
            return idx


def calculate_hash_v1(data):
    return calculate_hash(data, '00000')


def calculate_hash_v2(data):
    return calculate_hash(data, '000000')


def main():
    data = 'bgvyzdsv'
    res1 = calculate_hash_v1(data)
    print(res1)
    res2 = calculate_hash_v2(data)
    print(res2)


if __name__ == "__main__":
    main()

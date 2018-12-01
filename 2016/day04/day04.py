import collections
import string


def caesar_cipher(n):
    az = string.ascii_lowercase
    x = n % len(az)
    return str.maketrans(az, az[x:] + az[:x])


def decrypt(password):
    lst = password.split("-")
    phrase = "".join(lst[:-1])
    sid, crc = lst[-1][:-1].split("[")

    tops = [ (-n, c) for c, n in collections.Counter(phrase).most_common() ]
    ranked = ''.join(c for n, c in sorted(tops))

    if ranked.startswith(crc):
        return int(sid)

    return 0


def decode(password):
    lst = password.split("-")
    phrase = "".join(lst[:-1])
    sid, crc = lst[-1][:-1].split("[")

    phrase = password.translate(caesar_cipher(int(sid)))
    return phrase, sid



def main():
    data = [ line.rstrip("\n") for line in open("input04") ]

    res = 0
    for item in data:
        res += decrypt(item)
    print(res)


    for item in data:
        phr, sid = decode(item)
        if phr.startswith("north"):
            print(sid)
            break


if __name__ == "__main__":
    main()

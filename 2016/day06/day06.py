import collections


def decrypt(data):
    message1 = ""
    message2 = ""
    flist = [ "" ] * len(data[0])
    for item in data:
        for idx, c in enumerate(item):
            flist[idx] += c
    for item in flist:
        letters = collections.Counter(item).most_common()
        message1 += letters[0][0]
        message2 += letters[-1][0]
    return message1, message2


def main():
    data = [ line.rstrip("\n") for line in open("input06") ]
   
    msg1, msg2 = decrypt(data)
    print(msg1)
    print(msg2)   


if __name__ == "__main__":
    main()

def test_partA():
    data = [3, 4, 1, 5]
    assert(hashCheckSum(5, data) == 12)


def test_partB():
    assert(hashString("") == "a2582a3a0e66e6e86e3812dcb672a272")
    assert(hashString("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd")
    assert(hashString("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d")
    assert(hashString("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e")




def hashCheckSum(hashLen, seq):
    hl = HashList(hashLen)
    hl.conversion(seq)
    return hl.checkSum()


def hashString(text):
    hl = HashList(256)
    return hl.hashString(text)



class HashList:
    def __init__(self, len):
        self.length = len
        self.data = []
        for i in range(0, self.length):
            self.data.append(i)
        self.skip = 0
        self.cursor = 0


    def conversion(self, data):
        for value in data:
            sublist = self.sublist(self.cursor, value)
            self.update(self.cursor, sublist)

            self.cursor = self.cursor + value + self.skip 
            while self.cursor >= self.length:
                self.cursor -= self.length
            self.skip += 1



    def sublist(self, pos, length):
        sublist = []
        if pos + length < self.length:
            sublist = self.data[pos:pos+length]
        else:
            sublist = self.data[pos:] + self.data[:(pos + length - self.length)]
        sublist.reverse()
        return sublist


    def update(self, pos, sublist):
        for item in sublist:
            while pos >= self.length:
                pos = pos - self.length
            self.data[pos] = item
            pos += 1


    def checkSum(self):
        return (self.data[0] * self.data[1])


    def hashString(self, text):
        data = [ord(c) for c in text]
        data += [ 17, 31, 73, 47, 23 ]
        for i in range(0, 64):
            self.conversion(data)

        res = ""
        for i in range(0, 16):
            subdata = self.data[i*16:i*16+16]
            xor = 0
            for v in subdata:
                xor = xor ^ v
            res += "{:02x}".format(xor)
        return res


def main():
    with open('input10', 'r') as file:
        content = file.read().rstrip("\n")
        seq = [int(x) for x in content.split(",")]
        print(hashCheckSum(256, seq))
        print(hashString(content))


if __name__ == "__main__":
    main()

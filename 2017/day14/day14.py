def test_partA():
    assert(gridUsage("flqrgnkx") == 8108)


def test_partB():
    assert(countRegions("flqrgnkx") == 1242)


def gridUsage(data):
    res = 0
    for i in range(0, 128):
        line = "{}-{}".format(data, i)
        hashHex = HashList.hashString(line)
        hashBin = bin(int(hashHex, 16))[2:]
        hashBin = hashBin.zfill(128)
        for ch in hashBin:
            if ch == '1':
                res += 1
    return res


def findCell(row, col, data):
    while row < 128:
        while col < 128:
            if data[row][col] == "1":
                return row, col
            col += 1
        col = 0
        row += 1
    return None, None


def countRegions(data):
    res = 0
    hashList = []
    for i in range(0, 128):
        line = "{}-{}".format(data, i)
        hashHex = HashList.hashString(line)
        hashBin = bin(int(hashHex, 16))[2:]
        hashBin = hashBin.zfill(128)
        hashList.append(list(hashBin))

    row = 0
    col = 0
    row, col = findCell(row, col, hashList)
    while row != None:
        cellList = []
        cellList.append([row, col])
        while cellList:
            cell = cellList.pop(0)
            cellRow = cell[0]
            cellCol = cell[1]
            hashList[cellRow][cellCol] = "0"
            if (cellRow - 1 >= 0) and (hashList[cellRow - 1][cellCol] == "1"):
                cellList.append([cellRow - 1, cellCol])
            if (cellRow + 1 < 128) and (hashList[cellRow + 1][cellCol] == "1"):
                cellList.append([cellRow + 1, cellCol])
            if (cellCol - 1 >= 0) and (hashList[cellRow][cellCol - 1] == "1"):
                cellList.append([cellRow, cellCol - 1])
            if (cellCol + 1 < 128) and (hashList[cellRow][cellCol + 1] == "1"):
                cellList.append([cellRow, cellCol + 1])
        res += 1
        row, col = findCell(row, col, hashList)

    return res


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


    @staticmethod
    def hashString(text):
        hl = HashList(256)

        data = [ord(c) for c in text]
        data += [ 17, 31, 73, 47, 23 ]
        for i in range(0, 64):
            hl.conversion(data)

        res = ""
        for i in range(0, 16):
            subdata = hl.data[i*16:i*16+16]
            xor = 0
            for v in subdata:
                xor = xor ^ v
            res += "{:02x}".format(xor)
        return res


def main():
    print(gridUsage("vbqugkhl"))
    print(countRegions("vbqugkhl"))


if __name__ == "__main__":
    main()

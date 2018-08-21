import math

from enum import Enum


class SpiralListException(Exception):
    pass


class SliceSide(Enum):
    Right = 1
    Top = 2
    Left = 3
    Bottom = 4


class SpiralListSlice:
    def __init__(self, sliceNum):
        if sliceNum < 1:
            raise SpiralListException("Slice number should be greater than 0")

        self.sliceNum = sliceNum
        self.sliceWidth = (2 * self.sliceNum + 1)
        self.sliceEnd = (self.sliceWidth * self.sliceWidth)
        self.sliceStart = (self.sliceEnd - 8 * self.sliceNum + 1)


    def TR(self):
        return (self.sliceEnd - 3 * self.sliceWidth + 3)


    def TL(self):
        return (self.sliceEnd - 2 * self.sliceWidth + 2)


    def BL(self):
        return (self.sliceEnd - self.sliceWidth + 1)


    def BR(self):
        return self.sliceEnd


    def getSliceSide(self, slide):
        side = []
        if slide == SliceSide.Right:
            side.append(self.sliceEnd)
            for i in range(self.sliceStart, self.TR() + 1):
                side.append(i)
        elif slide ==SliceSide.Top:
            for i in range(self.TL(), self.TR() - 1, -1):
                side.append(i)
        elif slide ==SliceSide.Left:
            for i in range(self.BL(), self.TL() - 1, -1):
                side.append(i)
        elif slide ==SliceSide.Bottom:
            for i in range(self.BL(), self.BR() + 1):
                side.append(i)
        return side


    def getCellNumber(self, col, row):
        if abs(col) > self.sliceNum:
            raise SpiralListException("Column is greater than slice number")
        if abs(row) > self.sliceNum:
            raise SpiralListException("Row is greater than slice number")

        if abs(row) == abs(col):
            return self.getSliceCorner(col, row)

        return self.getSliceCell(col, row)


    def getSliceCorner(self, col, row):
        if col > 0 and row > 0:     # Top-Right
            return self.TR()
        if col > 0 and row < 0:     # Bottom-Right
            return self.BR()
        if col < 0 and row < 0:     # Bottom-Left
            return self.BL()
        if col < 0 and row > 0:     # Top-Left
            return self.TL()


    def getSliceCell(self, col, row):
        sliceSide = []
        if abs(col) == self.sliceNum:   # Vertical
            if col < 0:                 # Left
                sliceSide = self.getSliceSide(SliceSide.Left)
            if col > 0:                 # Right
                sliceSide = self.getSliceSide(SliceSide.Right)
            return sliceSide[row + self.sliceNum]
        if abs(row) == self.sliceNum:   # Horizontal
            if row < 0:                 # Bottom
                sliceSide = self.getSliceSide(SliceSide.Bottom)
            if row > 0:                 # Top
                sliceSide = self.getSliceSide(SliceSide.Top)
            return sliceSide[col + self.sliceNum]


    def getCellCoords(self, num):
        col = 0
        row = 0
        if num >= self.sliceStart and num <= self.TR():
            col = self.sliceNum
            row = self.getSliceSide(SliceSide.Right).index(num) - self.sliceNum
        elif num >= self.TR() and num <= self.TL():
            row = self.sliceNum
            col = self.getSliceSide(SliceSide.Top).index(num) - self.sliceNum
        elif num >= self.TL() and num <=self.BL():
            col = self.sliceNum * (-1)
            row = self.getSliceSide(SliceSide.Left).index(num) - self.sliceNum
        elif num >= self.BL() and num <= self.BR():
            row = self.sliceNum * (-1)
            col = self.getSliceSide(SliceSide.Bottom).index(num) - self.sliceNum

        return col, row



class SpiralListCell:
    def __init__(self, num=None, col=None, row=None):
        if num == None:
            self.cellColumn = col
            self.cellRow = row
            self.cellNumber = self.numberFromCoords(col, row)
        else:
            self.cellNumber = num
            self.cellColumn, self.cellRow = self.coordsFromNumber(num)


    def numberFromCoords(self, col, row):
        if col == None: 
            raise SpiralListException("Column not specified")
        if row == None: 
            raise SpiralListException("Row not specified")

        if col == 0 and row == 0:
            return 1

        sliceNum = abs(max(col, row, key=abs))
        slSlice = SpiralListSlice(sliceNum)
        return slSlice.getCellNumber(col, row)


    def sliceNum(self, value):
        res = math.sqrt(value)
        res = math.ceil(res)
        res = (res - 1) / 2
        res = math.ceil(res)
        return int(res)


    def coordsFromNumber(self, num):
        sliceNum = self.sliceNum(num)
        slSlice = SpiralListSlice(sliceNum)
        return slSlice.getCellCoords(num)


    def getCellNeighbors(self):
        cells = []
        cells.append(SpiralListCell(col=self.cellColumn+1, row=self.cellRow))
        cells.append(SpiralListCell(col=self.cellColumn+1, row=self.cellRow+1))
        cells.append(SpiralListCell(col=self.cellColumn,   row=self.cellRow+1))
        cells.append(SpiralListCell(col=self.cellColumn-1, row=self.cellRow+1))
        cells.append(SpiralListCell(col=self.cellColumn-1, row=self.cellRow))
        cells.append(SpiralListCell(col=self.cellColumn-1, row=self.cellRow-1))
        cells.append(SpiralListCell(col=self.cellColumn,   row=self.cellRow-1))
        cells.append(SpiralListCell(col=self.cellColumn+1, row=self.cellRow-1))

        res = []
        for c in cells:
            if c.cellNumber < self.cellNumber:
                res.append(c.cellNumber)
        return res


    def distance(self):
        w = abs(self.cellColumn)
        h = abs(self.cellRow)
        return (w + h)



class SpiralList:
    def __init__(self):
        self.data = [ 0, 1 ]


    def getCellValue(self, cell):
        if cell <= 0:
            raise SpiralListException("Bad cell index")

        if cell < len(self.data):
            return self.data[cell]
        if cell == len(self.data):
            slc = SpiralListCell(num=cell)
            cells = slc.getCellNeighbors()
            res = 0
            for c in cells:
                res += self.data[c]
            self.data.append(res)
            return res

        raise SpiralListException("Unable to count value")



def main():
    '''
    print(SpiralListCell(col=0, row=0).cellNumber)

    print(SpiralListCell(col=1, row=0).cellNumber)
    print(SpiralListCell(col=1, row=1).cellNumber)
    print(SpiralListCell(col=0, row=1).cellNumber)
    print(SpiralListCell(col=-1, row=1).cellNumber)
    print(SpiralListCell(col=-1, row=0).cellNumber)
    print(SpiralListCell(col=-1, row=-1).cellNumber)
    print(SpiralListCell(col=0, row=-1).cellNumber)
    print(SpiralListCell(col=1, row=-1).cellNumber)

    print(SpiralListCell(col=2, row=-1).cellNumber)
    print(SpiralListCell(col=2, row=0).cellNumber)
    print(SpiralListCell(col=2, row=1).cellNumber)
    print(SpiralListCell(col=2, row=2).cellNumber)
    print(SpiralListCell(col=1, row=2).cellNumber)
    print(SpiralListCell(col=0, row=2).cellNumber)
    print(SpiralListCell(col=-1, row=2).cellNumber)
    print(SpiralListCell(col=-2, row=2).cellNumber)
    print(SpiralListCell(col=-2, row=1).cellNumber)
    print(SpiralListCell(col=-2, row=0).cellNumber)
    print(SpiralListCell(col=-2, row=-1).cellNumber)
    print(SpiralListCell(col=-2, row=-2).cellNumber)
    print(SpiralListCell(col=-1, row=-2).cellNumber)
    print(SpiralListCell(col=0, row=-2).cellNumber)
    print(SpiralListCell(col=1, row=-2).cellNumber)
    print(SpiralListCell(col=2, row=-2).cellNumber)
    '''

    print("Distance 12 = {}".format(SpiralListCell(12).distance()))
    print("Distance 23 = {}".format(SpiralListCell(23).distance()))
    print("Distance 1024 = {}".format(SpiralListCell(1024).distance()))

    print("Distance 347991 = {}".format(SpiralListCell(347991).distance()))


    sl = SpiralList()
    ci = 1
    while True:
        res = sl.getCellValue(ci)
        ci += 1
        if res > 347991:
            print(res)
            break


if __name__ == "__main__":
    main()
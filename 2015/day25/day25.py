def getCell(row, column):
    #base = columnBase(row)
    #mod = rowMod(row, column)
    base = rowBase(column)
    mod = columnMod(row, column)
    return base + mod


def getValue(cell):
    value = 20151125
    for i in range(1, cell):
        value = value * 252533 % 33554393
    return value


def columnBase(row):
    base = 1
    for r in range(1, row):
        base += r
    return base


def columnMod(row, column):
    baseMod = column
    mod = 0
    for r in range(1, row):
        mod += baseMod
        baseMod += 1
    return mod


def rowBase(column):
    base = 0
    for c in range(0, column):
        base += (c + 1)
    return base


def rowMod(row, column):
    baseMod = row + 1
    mod = 0
    for c in range(1, column):
        mod += baseMod
        baseMod += 1
    return mod


def main():
    row = 3010
    column = 3019

    cell = getCell(row, column)
    crc = getValue(cell)
    print(crc)


if __name__ == "__main__":
    main()

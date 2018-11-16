def calculateA(data):
    grid = [ [ 0 for x in range(1000) ] for y in range(1000) ] 
    for item in data:
        lst = item.split(" ")
        if item.startswith("turn"):
            x1, y1 = lst[2].split(",")
            x2, y2 = lst[4].split(",")
            if lst[1] == "off":
                value = 0
            else:
                value = 1
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    grid[x][y] = value
        elif item.startswith("toggle"):
            x1, y1 = lst[1].split(",")
            x2, y2 = lst[3].split(",")
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    if grid[x][y] == 1:
                        grid[x][y] = 0
                    else:
                        grid[x][y] = 1

    res = 0
    for x in range(1000):
        for y in range(1000):
            res += grid[x][y]
    return res


def calculateB(data):
    grid = [ [ 0 for x in range(1000) ] for y in range(1000) ] 
    for item in data:
        lst = item.split(" ")
        if item.startswith("turn"):
            x1, y1 = lst[2].split(",")
            x2, y2 = lst[4].split(",")
            if lst[1] == "off":
                value = -1
            else:
                value = 1
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    grid[x][y] += value
                    if grid[x][y] < 0:
                        grid[x][y] = 0
        elif item.startswith("toggle"):
            x1, y1 = lst[1].split(",")
            x2, y2 = lst[3].split(",")
            for x in range(int(x1), int(x2) + 1):
                for y in range(int(y1), int(y2) + 1):
                    grid[x][y] += 2
                    
    res = 0
    for x in range(1000):
        for y in range(1000):
            res += grid[x][y]
    return res


def main():
    data = [ line.rstrip("\n") for line in open("input06") ]
    res1 = calculateA(data)
    res2 = calculateB(data)
    print(res1, res2)


if __name__ == "__main__":
    main()

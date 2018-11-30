directions = {
    "N": ("W", "E"),
    "S": ("E", "W"),
    "E": ("N", "S"),
    "W": ("S", "N")
}


def distanceA(path):
    direction = "N"
    location = [ 0, 0 ]
    for item in path:
        if item[0] == "R":
            direction = directions[direction][1]
        else:
            direction = directions[direction][0]
        steps = int(item[1:])
        if direction == "N":
            location[1] += steps
        elif direction == "S":
            location[1] -= steps
        elif direction == "E":
            location[0] += steps
        elif direction == "W":
            location[0] -= steps
    return (abs(location[0]) + abs(location[1]))


def distanceB(path):
    direction = "N"
    location = [ 0, 0 ]
    locations = [ location.copy() ]
    for item in path:
        if item[0] == "R":
            direction = directions[direction][1]
        else:
            direction = directions[direction][0]
        steps = int(item[1:])
        if direction == "N":
            for i in range(steps):
                location[1] += 1
                if location not in locations:
                    locations.append(location.copy())
                else:
                    return (abs(location[0]) + abs(location[1]))
        elif direction == "S":
            for i in range(steps):
                location[1] -= 1
                if location not in locations:
                    locations.append(location.copy())
                else:
                    return (abs(location[0]) + abs(location[1]))
        elif direction == "E":
            for i in range(steps):
                location[0] += 1
                if location not in locations:
                    locations.append(location.copy())
                else:
                    return (abs(location[0]) + abs(location[1]))
        elif direction == "W":
            for i in range(steps):
                location[0] -= 1
                if location not in locations:
                    locations.append(location.copy())
                else:
                    return (abs(location[0]) + abs(location[1]))


def main():
    content = open("input01").read().rstrip("\n").split(", ")
    
    print(distanceA(content))
    print(distanceB(content))


if __name__ == "__main__":
    main()

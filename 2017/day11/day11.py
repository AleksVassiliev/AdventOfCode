def test_partA():
    assert(stepsCount("ne,ne,ne") == 3)
    assert(stepsCount("ne,ne,sw,sw") == 0)
    assert(stepsCount("ne,ne,s,s") == 2)
    assert(stepsCount("se,sw,se,sw,sw") == 3)

'''
pathBack = [ ["n", "s"], ["ne", "sw"], ["nw", "se"] ]
pathSide = { "n": ["nw", "ne"], "ne": ["n", "se"], "se": ["ne", "s"], "s": ["se", "sw"], "sw": ["s", "nw"], "nw": ["sw", "n"] }


def isBackStep(prevStep, step):
    if prevStep != step:
        for path in pathBack:
            if (prevStep in path) and (step in path):
                return True
    return False


def isSideStep(prevStep, step):
    path = pathSide[step]
    if prevStep in path:
        return True
    return False


def getStepDistance(prevStep, step):
    if isBackStep(prevStep, step) == True:
        return -1
    elif isSideStep(prevStep, step) == True:
        return 0
    else:
        return 1


def stepsCount(path):
    steps = path.split(",")
    prevStep = steps[0]
    distance = 1
    for step in steps[1:]:
        distance += getStepDistance(prevStep, step)
        prevStep = step
    return distance
'''

movement = { "n":  [  1, -1,  0 ],
             "ne": [  1,  0, -1 ],
             "se": [  0,  1, -1 ],
             "s":  [ -1,  1,  0 ],
             "sw": [ -1,  0,  1 ],
             "nw": [  0, -1,  1 ]      
           }


class HexCell:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0


    def move(self, direction):
        step = movement[direction]
        self.x += step[0]
        self.y += step[1]
        self.z += step[2]


    def distance(self):
        return abs(max([self.x, self.y, self.z], key=abs))



def stepsCount(path):
    steps = path.split(",")
    cell = HexCell()
    maxCell = 0
    for step in steps:
        cell.move(step)
        maxCell = max(maxCell, cell.distance())
    return cell.distance(), maxCell


def main():
    with open("input11", "r") as f:
        content = f.read().rstrip("\n")
        print(stepsCount(content))


if __name__ == "__main__":
    main()

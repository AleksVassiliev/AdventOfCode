pipes = [ '0 <-> 2',
          '1 <-> 1',
          '2 <-> 0, 3, 4',
          '3 <-> 2, 4',
          '4 <-> 2, 3, 6',
          '5 <-> 6',
          '6 <-> 4, 5'
        ]


def test_partA():
    assert(getProgramsLen(pipes, "0") == 6)


def test_partB():
    assert(getGroupsLen(pipes) == 2)



def getProgramsLen(data, value):
    programs = getPrograms(data, value)
    return len(programs)


def getPrograms(data, value):
    programs = set()
    pipes = {}
    for d in data:
        pipe = d.split(" <-> ")
        src = pipe[0]
        dst = pipe[1]
        pipes[src] = dst.split(", ")

    child = []
    while True:
        programs.add(value)
        for v in pipes[value]:
            if (v not in child) and (v not in programs):
                child.append(v)

        if not child:
            return programs

        value = child.pop(0)


def getGroupsLen(data):
    programs = set()
    pipes = {}
    for d in data:
        pipe = d.split(" <-> ")
        src = pipe[0]
        dst = pipe[1]
        pipes[src] = dst.split(", ")

    groupsLen = 0
    while pipes:
        key = list(pipes.keys())[0]
        programs = getPrograms(data, key)
        for p in programs:
            pipes.pop(p)
        groupsLen += 1

    return groupsLen


def main():
    content = [ line.rstrip('\n') for line in open('input12') ]

    print(getProgramsLen(content, "0"))
    print(getGroupsLen(content))


if __name__ == "__main__":
    main()
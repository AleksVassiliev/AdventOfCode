import operator
import functools
import itertools


def qe(data, groups):
    size = sum(data) // groups
    for i in range(len(data)):
        #qes = [ functools.reduce(operator.mul, c) for c in itertools.combinations(data, i) if sum(c) == size ]
        qes = []
        for c in itertools.combinations(data, i):
            if sum(c) == size:
                qes.append(functools.reduce(operator.mul, c))
        if qes:
            return min(qes)
    return None


def main():
    data = [ int(line.strip("\n")) for line in open("input24") ]

    print(qe(data, 3))
    print(qe(data, 4))


if __name__ == "__main__":
    main()

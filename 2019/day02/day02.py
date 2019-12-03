import copy

def process(data):
    pc = 0
    while data[pc] != 99:
        opcode = data[pc]
        value0 = data[pc+1]
        value1 = data[pc+2]
        res = data[pc+3]
        if opcode == 1:
            data[res] = data[value0] + data[value1]
        elif opcode == 2:
            data[res] = data[value0] * data[value1]
        pc = pc + 4
    return data[0]


def part1(data):
    current = copy.copy(data)
    current[1] = 12
    current[2] = 2
    return process(current)

def part2(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            current = copy.copy(data)
            current[1] = noun
            current[2] = verb
            res = process(current)
            if res == 19690720:
                return 100 * noun + verb

def main():
    content = open('input02').read().rstrip('\n').split(',')
    data = [ int(x) for x in content ]
    
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()

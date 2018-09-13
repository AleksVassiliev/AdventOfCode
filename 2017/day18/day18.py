def test_partA():
    program = [ "set a 1",
                "add a 2",
                "mul a a",
                "mod a 5",
                "snd a",
                "set a 0",
                "rcv a",
                "jgz a -1",
                "set a 1",
                "jgz a -2"
               ]

    assert(executeA(program) == 4)


def test_partB():
    program = [ "snd 1",
                "snd 2",
                "snd p",
                "rcv a",
                "rcv b",
                "rcv c",
                "rcv d"
              ]

    assert(executeB(program) == 3)


def executeA(program):
    registers = {}
    frequency = 0
    cursor = 0
    while True:
        ops = program[cursor].split(" ")
        op = ops[0]
        reg = ops[1]

        if op == "snd":
            frequency = registers[reg]
            cursor += 1
        
        elif op == "set":
            value = ops[2]
            try:
                registers[reg] = int(value)
            except ValueError:
                registers[reg] = registers[value]
            cursor += 1
        
        elif op == "add":
            value = ops[2]
            try:
                value = int(value)
            except ValueError:
                value = registers[value]
            registers[reg] += value
            cursor += 1
        
        elif op == "mul":
            if reg not in registers:
                registers[reg] = 0
            value = ops[2]
            try:
                value = int(value)
            except ValueError:
                value = registers[value]
            registers[reg] *= value
            cursor += 1
        
        elif op == "mod":
            value = ops[2]
            try:
                value = int(value)
            except ValueError:
                value = registers[value]
            registers[reg] %= value
            cursor += 1
        
        elif op == "rcv":
            if value != 0:
                return frequency
            cursor += 1
        
        elif op == "jgz":
            value = ops[2]
            if registers[reg] > 0:
                try:
                    value = int(value)
                except ValueError:
                    value = registers[value]
                cursor += value
            else:
                cursor += 1


def executeB(program):
    pass


def main():
    program = [ line.rstrip('\n') for line in open('input18') ]
    print(executeA(program))
    print(executeB(program))


if __name__ == "__main__":
    main()

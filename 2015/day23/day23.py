def execute(program, initial):
    regs = {
        "a": initial,
        "b": 0
    }

    pc = 0
    while pc < len(program):
        line = program[pc]
        instr = line[:3]
        if instr == "hlf":
            r = line[4]
            regs[r] = regs[r] / 2
            pc += 1
        elif instr == "tpl":
            r = line[4]
            regs[r] = regs[r] * 3
            pc += 1
        elif instr == "inc":
            r = line[4]
            regs[r] = regs[r] + 1
            pc += 1
        elif instr == "jmp":
            offset = line.split(" ")[1]
            pc += int(offset)
        elif instr == "jie":
            r, offset = line[4:].split(", ")
            if regs[r] % 2 == 0:
                pc += int(offset)
            else:
                pc += 1
        elif instr == "jio":
            r, offset = line[4:].split(", ")
            if regs[r] == 1:
                pc += int(offset)
            else:
                pc += 1

    return regs["b"]


def main():
    program = [ line.strip("\n") for line in open("input23") ]
    
    res = execute(program, 0)
    print(res)

    res = execute(program, 1)
    print(res)
    

if __name__ == "__main__":
    main()

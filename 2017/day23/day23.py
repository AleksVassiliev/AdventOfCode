class Coprocessor:
    def __init__(self):
        self.registers = {}


    def initialize(self):
        self.registers['a'] = 0
        self.registers['b'] = 0
        self.registers['c'] = 0
        self.registers['d'] = 0
        self.registers['e'] = 0
        self.registers['f'] = 0
        self.registers['g'] = 0
        self.registers['h'] = 0
        self.pcounter = 0


    def get(self, value):
        if value in 'abcdefgh':
            return self.registers[value]
        return int(value)


    def execute1(self, program):
        self.initialize()
        counter = 0
        plen = len(program)
        while self.pcounter < plen:
            instr, x, y = program[self.pcounter].split(" ")
            if instr == "set":
                self.registers[x] = self.get(y)
                self.pcounter += 1
            elif instr == "sub":
                self.registers[x] -= self.get(y)
                self.pcounter += 1
            elif instr == "mul":
                self.registers[x] *= self.get(y)
                self.pcounter += 1
                counter += 1
            elif instr == "jnz":
                if self.get(x) != 0:
                    self.pcounter += self.get(y)
                else:
                    self.pcounter += 1
        return counter


def check(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def execute2():
    b = 107900
    c = 124900
    h = 0
    for v in range(b, c + 1, 17):
        if not check(v):
            h += 1
    return h




def main():
    program = [ line.rstrip("\n") for line in open("input23") ]

    cpu = Coprocessor()
    res = cpu.execute1(program)
    print(res)
    
    res = execute2()
    print(res)
    

if __name__ == "__main__":
    main()

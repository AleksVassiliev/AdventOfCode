testData = [ "b inc 5 if a > 1",
             "a inc 1 if b < 5",
             "c dec -10 if a >= 1",
             "c inc -20 if c == 10"
           ]


def test_partA():
    program = Program(testData)
    program.execute()
    assert(program.maximum() == 1)


def test_partB():
    program = Program(testData)
    program.execute()
    assert(program.regMax == 10)



class Program:
    def __init__(self, program):
        self.program = program
        self.registers = {}
        self.regMax = 0


    def maximum(self):
        registers = []
        for k in self.registers:
            registers.append(self.registers[k])
        registers.sort(reverse=True)

        return registers[0]


    def execute(self):
        for line in self.program:
            value = line.split(" if ")
            instr = value[0]
            cond = value[1]
            if self.condition(cond) == True:
                self.instruction(instr)
            
            self.regMax = max(self.regMax, self.maximum())


    def condition(self, cond):
        values = cond.split(" ")
        reg = values[0]
        condition = values[1]
        value = int(values[2])

        if reg not in self.registers:
            self.registers[reg] = 0

        if condition == "==":
            return (self.registers[reg] == value)
        elif condition == "!=":
            return (self.registers[reg] != value)
        elif condition == ">":
            return (self.registers[reg] > value)
        elif condition == ">=":
            return (self.registers[reg] >= value)
        elif condition == "<":
            return (self.registers[reg] < value)
        elif condition == "<=":
            return (self.registers[reg] <= value)
        else:
            return False


    def instruction(self, instr):
        values = instr.split(" ")
        reg = values[0]
        operation = values[1]
        value = int(values[2])

        if reg not in self.registers:
            self.registers[reg] = 0

        if operation == "dec":
            self.registers[reg] -= value
        elif operation == "inc":
            self.registers[reg] += value



def main():
    content = [ line.rstrip('\n') for line in open('input08') ]

    program = Program(content)
    program.execute()

    print(program.maximum())
    print(program.regMax)

    
if __name__ == "__main__":
    main()

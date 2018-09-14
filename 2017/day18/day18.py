import collections

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


class ThreadA:
    def __init__(self):
        self.registers = collections.defaultdict(int)


    def get(self, value):
        if value in "abcdefghijklmnopqrstuvwxyz":
            return self.registers[value]
        return int(value)


    def execute(self, program):
        frequency = 0
        index = 0
        while True:
            instr = program[index].split(" ")
            if instr[0] == "snd":
                frequency = self.registers[instr[1]]        
            elif instr[0] == "set":
                self.registers[instr[1]] = self.get(instr[2])        
            elif instr[0] == "add":
                self.registers[instr[1]] += self.get(instr[2])        
            elif instr[0] == "mul":
                self.registers[instr[1]] *= self.get(instr[2])        
            elif instr[0] == "mod":
                self.registers[instr[1]] %= self.get(instr[2])        
            elif instr[0] == "rcv":
                if self.registers[instr[1]] != 0:
                    return frequency        
            elif instr[0] == "jgz":
                if self.get(instr[1]) > 0:
                    index += self.get(instr[2]) - 1
            index += 1


def executeA(program):
    t = ThreadA()
    res = t.execute(program)
    return res



class ThreadB:
    def __init__(self, tid, program):
        self.registers = collections.defaultdict(int)
        self.registers["p"] = tid
        self.index = 0
        self.program = program
        self.counter = 0
        self.tid = tid


    def get(self, value):
        if value in "abcdefghijklmnopqrstuvwxyz":
            return self.registers[value]
        return int(value)


    def execute(self, inqueue):
        outqueue = []
        while True:
            instr = self.program[self.index].split(" ")
            if instr[0] == "snd":
                outqueue.append(self.registers[instr[1]])
                self.counter += 1        
            elif instr[0] == "set":
                self.registers[instr[1]] = self.get(instr[2])        
            elif instr[0] == "add":
                self.registers[instr[1]] += self.get(instr[2])        
            elif instr[0] == "mul":
                self.registers[instr[1]] *= self.get(instr[2])        
            elif instr[0] == "mod":
                self.registers[instr[1]] %= self.get(instr[2])        
            elif instr[0] == "rcv":
                if not inqueue:
                    return outqueue
                else:
                    self.registers[instr[1]] = inqueue.pop(0)        
            elif instr[0] == "jgz":
                if self.get(instr[1]) > 0:
                    self.index += self.get(instr[2]) - 1
            self.index += 1



def executeB(program):
    a = ThreadB(0, program)
    b = ThreadB(1, program)

    queue = []
    while True:
        queue = a.execute(queue)
        queue = b.execute(queue)

        if not queue:
            return b.counter


def main():
    program = [ line.rstrip('\n') for line in open('input18') ]
    print(executeA(program))
    print(executeB(program))


if __name__ == "__main__":
    main()

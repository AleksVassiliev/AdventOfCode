class Program:
    def __init__(self, program):
        self._program = program
        self._ip = 0
        self._ops = set()
        self._acc = 0

    def execute(self):
        self._ip = 0
        self._acc = 0
        self._ops.clear()
        while True:
            if self._ip in self._ops:
                return False
            self._ops.add(self._ip)
            line = self._program[self._ip]
            op, value = line.split(' ')
            value = int(value)
            if op == 'nop':
                self._ip += 1
            elif op == 'jmp':
                self._ip += value
            elif op == 'acc':
                self._ip += 1
                self._acc += value
            if self._ip >= len(self._program):
                return True

    def safe_execute(self):
        pos = -1
        while pos < len(self._program):
            for i in range(pos + 1, len(self._program)):
                pos = i
                if self._program[i].startswith('jmp'):
                    self._program[i] = self._program[i].replace('jmp', 'nop')
                    break
                if self._program[i].startswith('nop'):
                    self._program[i] = self._program[i].replace('nop', 'jmp')
                    break

            res = self.execute()
            if res == True:
                break

            if self._program[pos].startswith('jmp'):
                self._program[pos] = self._program[pos].replace('jmp', 'nop')
            elif self._program[pos].startswith('nop'):
                self._program[pos] = self._program[pos].replace('nop', 'jmp')

    @property
    def acc(self):
        return self._acc


def execute(program):
    p = Program(program)
    p.execute()
    return p.acc


def safe_execute(program):
    p = Program(program)
    p.safe_execute()
    return p.acc


def main():
    program = [line.strip() for line in open('./input08.txt')]
    result_v1 = execute(program)
    print(result_v1)
    result_v2 = safe_execute(program)
    print(result_v2)


if __name__ == '__main__':
    main()

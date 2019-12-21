import sys
import copy
import itertools
import collections

from enum import Enum


class State(Enum):
    EWorking = 0,
    EWaitForInput = 1,
    ERaiseOutput = 2,
    EHalted = 3


class Opcode:
    def __init__(self, value):
        self.opcode = value % 100
        self.mode1 = value // 100 % 10
        self.mode2 = value // 1000 % 10
        self.mode3 = value // 10000 % 10


class Computer:
    def __init__(self, data):
        self.data = copy.copy(data)
        self.input_params = collections.deque()
        self.output_params = collections.deque()
        self.instr_counter = 0
        self.relative_base = 0
        self.state = State.EWorking
        self.external_memory = collections.defaultdict(int)

    def add_input_param(self, value):
        self.input_params.append(value)

    def read(self, addr):
        try:
            return self.data[addr]
        except IndexError:
            return self.external_memory[addr]

    def write(self, addr, value):
        try:
            self.data[addr] = value
        except IndexError:
            self.external_memory[addr] = value

    def get_value(self, addr, mode):
        value = self.read(addr)
        if mode == 0:
            return self.read(value)
        if mode == 1:
            return value
        if mode == 2:
            return self.read(self.relative_base + value)

    def get_addr(self, addr, mode):
        value = self.read(addr)
        if mode == 2:
            return value + self.relative_base
        else:
            return value

    def opcode1(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        param2 = self.get_value(self.instr_counter+2, instr.mode2)
        param3 = self.get_addr(self.instr_counter+3, instr.mode3)
        self.write(param3, param1 + param2)
        self.instr_counter += 4

    def opcode2(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        param2 = self.get_value(self.instr_counter+2, instr.mode2)
        param3 = self.get_addr(self.instr_counter+3, instr.mode3)
        self.write(param3, param1 * param2)
        self.instr_counter += 4

    def opcode3(self, instr):
        param1 = self.get_addr(self.instr_counter+1, instr.mode1)
        try:
            self.write(param1, self.input_params.popleft())
            self.instr_counter += 2
        except IndexError:
            self.state = State.EWaitForInput

    def opcode4(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        self.output_params.append(param1)
        self.instr_counter += 2
        self.state = State.ERaiseOutput

    def opcode5(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        param2 = self.get_value(self.instr_counter+2, instr.mode2)
        if param1 != 0:
            self.instr_counter = param2
        else:
            self.instr_counter += 3

    def opcode6(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        param2 = self.get_value(self.instr_counter+2, instr.mode2)
        if param1 == 0:
            self.instr_counter = param2
        else:
            self.instr_counter += 3

    def opcode7(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        param2 = self.get_value(self.instr_counter+2, instr.mode2)
        param3 = self.get_addr(self.instr_counter+3, instr.mode3)
        if param1 < param2:
            self.write(param3, 1)
        else:
            self.write(param3, 0)
        self.instr_counter += 4

    def opcode8(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        param2 = self.get_value(self.instr_counter+2, instr.mode2)
        param3 = self.get_addr(self.instr_counter+3, instr.mode3)
        if param1 == param2:
            self.write(param3, 1)
        else:
            self.write(param3, 0)
        self.instr_counter += 4

    def opcode9(self, instr):
        param1 = self.get_value(self.instr_counter+1, instr.mode1)
        self.relative_base += param1
        self.instr_counter += 2

    def opcode99(self, instr):
        self.state = State.EHalted

    def process(self):
        self.state = State.EWorking
        instr = Opcode(self.data[self.instr_counter])
        if instr.opcode == 1:
            self.opcode1(instr)
        elif instr.opcode == 2:
            self.opcode2(instr)
        elif instr.opcode == 3:
            self.opcode3(instr)
        elif instr.opcode == 4:
            self.opcode4(instr)
        elif instr.opcode == 5:
            self.opcode5(instr)
        elif instr.opcode == 6:
            self.opcode6(instr)
        elif instr.opcode == 7:
            self.opcode7(instr)
        elif instr.opcode == 8:
            self.opcode8(instr)
        elif instr.opcode == 9:
            self.opcode9(instr)
        elif instr.opcode == 99:
            self.opcode99(instr)


class Direction(Enum):
    T = 0,
    B = 1,
    L = 2,
    R = 3

class Robot:
    map_moves = {
        Direction.T: [ (Direction.L, -1, 0), (Direction.R, 1, 0) ],
        Direction.B: [ (Direction.R, 1, 0), (Direction.L, -1, 0) ],
        Direction.L: [ (Direction.B, 0, 1), (Direction.T, 0, -1) ],
        Direction.R: [ (Direction.T, 0, -1), (Direction.B, 0, 1) ]
    } 

    def __init__(self, color):
        self.coord = (0, 0)
        self.grid = collections.defaultdict(int)
        self.grid[self.coord] = color
        self.direction = Direction.T
    
    def move(self, angle):
        m = self.map_moves[self.direction][angle]
        self.coord = (self.coord[0] + m[1], self.coord[1] + m[2])
        self.direction = m[0]

    def execute(self, program):
        c = Computer(program)
        op = collections.deque()
        while c.state != State.EHalted:
            if c.state == State.EWaitForInput:
                param = self.grid[self.coord]
                c.add_input_param(param)
            elif c.state == State.ERaiseOutput:
                op.append(c.output_params.popleft())
                if len(op) == 2:
                    self.grid[self.coord] = op.popleft()
                    self.move(op.popleft())
            c.process()
        return len(self.grid.keys())

    def dump(self):
        xmin = sys.maxsize
        xmax = 0
        ymin = sys.maxsize
        ymax = 0
        for k in self.grid:
            xmin, xmax = min(k[0], xmin), max(k[0], xmax)
            ymin, ymax = min(k[1], ymin), max(k[1], ymax)

        width = xmax - xmin + 1
        height = ymax - ymin + 1
        image = [ [' '] * width for i in range(height) ]

        for k in self.grid:
            if self.grid[k] == 1:
                x = k[0] - xmin
                y = k[1] - ymin
                image[y][x] = '#'

        for line in image:
            linerepr = ''
            for pixel in line:
                linerepr += pixel
            print(linerepr)


def main():
    content = open('input11').read().rstrip('\n').split(',')
    data = [ int(x) for x in content ]

    r = Robot(0)
    print(r.execute(data))

    r = Robot(1)
    r.execute(data)
    r.dump()


if __name__ == '__main__':
    main()

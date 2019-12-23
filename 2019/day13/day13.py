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


class GameState:
    def __init__(self):
        self.ball = None
        self.paddle = None
        self.score = None

    def process(self, params):
        while len(params) != 0:
            pos_x = params.popleft()
            pos_y = params.popleft()
            tile_id = params.popleft()
            if tile_id == 3:
                self.paddle = (pos_x, pos_y)
            elif tile_id == 4:
                self.ball = (pos_x, pos_y)
            elif (pos_x == -1) and (pos_y == 0):
                self.score = tile_id


def part1(program):
    c = Computer(program)
    while c.state != State.EHalted:
        c.process()
    
    block = 0
    while len(c.output_params) != 0:
        pos_x = c.output_params.popleft()
        pos_y = c.output_params.popleft()
        tile_id = c.output_params.popleft()
        if tile_id == 2:
            block += 1
    return block


def part2(program):
    program[0] = 2
    c = Computer(program)
    gs = GameState()
    while c.state != State.EHalted:
        if c.state == State.EWaitForInput:
            gs.process(c.output_params)
            if gs.paddle[0] < gs.ball[0]:
                c.add_input_param(1)
            elif gs.paddle[0] > gs.ball[0]:
                c.add_input_param(-1)
            else:
                c.add_input_param(0)
        c.process()
    gs.process(c.output_params)
    return gs.score

    
def main():
    content = open('input13').read().rstrip('\n').split(',')
    data = [ int(x) for x in content ]

    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()

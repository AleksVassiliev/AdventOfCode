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
        self.state = State.EWorking

    def add_input_param(self, value):
        self.input_params.append(value)

    def get_value(self, addr, mode):
        value = self.data[addr]
        if mode == 0:
            return self.data[value]
        if mode == 1:
            return value

    def opcode1(self, instr):
        addr = self.data[self.instr_counter+3]
        self.data[addr] = self.get_value(self.instr_counter+1, instr.mode1) + self.get_value(self.instr_counter+2, instr.mode2)
        self.instr_counter += 4

    def opcode2(self, instr):
        addr = self.data[self.instr_counter+3]
        self.data[addr] = self.get_value(self.instr_counter+1, instr.mode1) * self.get_value(self.instr_counter+2, instr.mode2)
        self.instr_counter += 4

    def opcode3(self, instr):
        addr = self.data[self.instr_counter+1]
        try:
            self.data[addr] = self.input_params.popleft()
            self.instr_counter += 2
        except IndexError:
            self.instr_counter += 2
            self.state = State.EWaitForInput

    def opcode4(self, instr):
        value = self.get_value(self.instr_counter+1, instr.mode1)
        self.output_params.append(value)
        self.instr_counter += 2
        self.state = State.ERaiseOutput

    def opcode5(self, instr):
        if self.get_value(self.instr_counter+1, instr.mode1) != 0:
            self.instr_counter = self.get_value(self.instr_counter+2, instr.mode2)
        else:
            self.instr_counter += 3

    def opcode6(self, instr):
        if self.get_value(self.instr_counter+1, instr.mode1) == 0:
            self.instr_counter = self.get_value(self.instr_counter+2, instr.mode2)
        else:
            self.instr_counter += 3

    def opcode7(self, instr):
        addr = self.data[self.instr_counter+3]
        if self.get_value(self.instr_counter+1, instr.mode1) < self.get_value(self.instr_counter+1, instr.mode1):
            self.data[addr] = 1
        else:
            self.data[addr] = 0
        self.instr_counter += 4

    def opcode8(self, instr):
        addr = self.data[self.instr_counter+3]
        if self.get_value(self.instr_counter+1, instr.mode1) == self.get_value(self.instr_counter+1, instr.mode1):
            self.data[addr] = 1
        else:
            self.data[addr] = 0
        self.instr_counter += 4

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
        elif instr.opcode == 99:
            self.opcode99(instr)


def process1(data, pset):
    param = 0
    for i in range(0, 5):
        amp = Computer(data)
        amp.add_input_param(pset[i])
        amp.add_input_param(param)
        while amp.state is not State.ERaiseOutput:
            amp.process()
        param = amp.output_params.popleft()
    return param    


def process2(data, pset):
    amps = []
    for i in range(5):
        amp = Computer(data)
        amp.add_input_param(pset[i])
        amps.append(amp)
    param = 0
    signal = 0
    while True:
        for i in range(0, 5):
            amps[i].add_input_param(param)
            while True:
                amps[i].process()
                if amps[i].state in [ State.ERaiseOutput, State.EHalted ]:
                    break
            if amps[i].state == State.ERaiseOutput:
                param = amps[i].output_params.popleft()
            else:
                return signal
            signal = max(signal, param)


def main():
    content = open('input07').read().rstrip('\n').split(',')    
    data = [ int(x) for x in content ]

    psets = [ list(x) for x in itertools.permutations([0, 1, 2, 3, 4])]
    signal = 0
    for pset in psets:
        res = process1(data, pset)
        signal = max(signal, res)
    print(signal)

    psets = [ list(x) for x in itertools.permutations([5, 6, 7, 8, 9])]
    signal = 0
    for pset in psets:
        res = process2(data, pset)
        signal = max(signal, res)
    print(signal)
    
    
if __name__ == '__main__':
    main()

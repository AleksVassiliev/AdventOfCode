import copy
import itertools
import collections


class Amplifier:
    def __init__(self, data, param):
        self.data = copy.copy(data)
        self.input_params = collections.deque([param])
        self.is_halted = False
        self.instr_counter = 0

    def process(self, param):
        self.input_params.append(param)
        output_param = None
        pc = self.instr_counter
        while self.is_halted == False:
            opcode = self.data[pc] % 100
            mode1 = self.data[pc] // 100 % 10
            mode2 = self.data[pc] // 1000 % 10
            mode3 = self.data[pc] // 10000 % 10
            if opcode == 1:
                value1 = self.data[pc+1]
                value2 = self.data[pc+2]
                res = self.data[pc+3]
                self.data[res] = (value1 if mode1 == 1 else self.data[value1]) + (value2 if mode2 == 1 else self.data[value2])
                pc += 4
            elif opcode == 2:
                value1 = self.data[pc+1]
                value2 = self.data[pc+2]
                res = self.data[pc+3]
                self.data[res] = (value1 if mode1 == 1 else self.data[value1]) * (value2 if mode2 == 1 else self.data[value2])
                pc += 4
            elif opcode == 3:
                res = self.data[pc+1]
                try:
                    self.data[res] = self.input_params.popleft()
                    pc += 2
                except IndexError:
                    self.instr_counter = pc + 2
                    break
            elif opcode == 4:
                res = self.data[pc+1]
                output_param = res if mode1 == 1 else self.data[res]
                self.instr_counter = pc + 2
                break
            elif opcode == 5:
                param1 = self.data[pc+1]
                param2 = self.data[pc+2]
                value = param1 if mode1 == 1 else self.data[param1]
                if value != 0:
                    pc = param2 if mode2 == 1 else self.data[param2]
                else:
                    pc += 3
            elif opcode == 6:
                param1 = self.data[pc+1]
                param2 = self.data[pc+2]
                value = param1 if mode1 == 1 else self.data[param1]
                if value == 0:
                    pc = param2 if mode2 == 1 else self.data[param2]
                else:
                    pc += 3
            elif opcode == 7:
                param1 = self.data[pc+1]
                param2 = self.data[pc+2]
                param3 = self.data[pc+3]
                value1 = param1 if mode1 == 1 else self.data[param1]
                value2 = param2 if mode2 == 1 else self.data[param2]
                if value1 < value2:
                    self.data[param3] = 1
                else:
                    self.data[param3] = 0
                pc += 4
            elif opcode == 8:
                param1 = self.data[pc+1]
                param2 = self.data[pc+2]
                param3 = self.data[pc+3]
                value1 = param1 if mode1 == 1 else self.data[param1]
                value2 = param2 if mode2 == 1 else self.data[param2]
                if value1 == value2:
                    self.data[param3] = 1
                else:
                    self.data[param3] = 0
                pc += 4
            elif opcode == 99:
                self.is_halted = True
        return output_param


def process2(data, pset):
    amps = [ Amplifier(data, x) for x in pset ]    
    param = 0
    signal = 0
    while True:
        for i in range(0, 5):
            param = amps[i].process(param)
            if param is None:
                return signal
            signal = max(signal, param)


def main():
    content = open('input07').read().rstrip('\n').split(',')    
    data = [ int(x) for x in content ]
    
    psets = [ list(x) for x in itertools.permutations([0, 1, 2, 3, 4])]
    signal = 0
    for pset in psets:
        param = 0
        for i in range(0, 5):
            amp = Amplifier(data, pset[i])
            param = amp.process(param)
        signal = max(signal, param)
    print(signal)

    psets = [ list(x) for x in itertools.permutations([5, 6, 7, 8, 9])]
    signal = 0
    for pset in psets:
        res = process2(data, pset)
        signal = max(signal, res)
    print(signal)
    
    
if __name__ == '__main__':
    main()

test_states = {
    "A": { 0: (1, +1, "B"), 1: (0, -1, "B") },
    "B": { 0: (1, -1, "A"), 1: (1, +1, "A") }
}

states = {
    "A": { 0: (1, +1, "B"), 1: (0, -1, "C") },
    "B": { 0: (1, -1, "A"), 1: (1, +1, "D") },
    "C": { 0: (0, -1, "B"), 1: (0, -1, "E") },
    "D": { 0: (1, +1, "A"), 1: (0, +1, "B") },
    "E": { 0: (1, -1, "F"), 1: (1, -1, "C") },
    "F": { 0: (1, +1, "D"), 1: (1, +1, "A") }
}


class TuringMachine:
    def __init__(self, states):
        self.states = states
        self.tape = [ 0 ]
        self.cursor = 0
        self.state = "A"


    def step(self):
        tape_value = self.tape[self.cursor]
        value, direction, state = self.states[self.state][tape_value]
        
        self.tape[self.cursor] = value        
        self.cursor += direction
        if self.cursor < 0:
            self.tape.insert(0, 0)
            self.cursor = 0
        elif self.cursor >= len(self.tape):
            self.tape.append(0)
        self.state = state


    def checksum(self):
        res = 0
        for i in self.tape:
            res += i
        return res


def main():
    '''
    tm = TuringMachine(test_states)
    for i in range(6):
        tm.step()
    print(tm.checksum())
    '''
    tm = TuringMachine(states)
    for i in range(12667664):
        tm.step()
    print(tm.checksum())

if __name__ == "__main__":
    main()
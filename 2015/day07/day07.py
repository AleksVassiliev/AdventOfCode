class Circuit:
    def __init__(self, circuit):
        self.wires = {}
        self.results = {}
        for item in circuit:
            l, wire = item.split(" -> ")
            self.wires[wire] = l.split(" ")


    def get_signal(self, wire):
        try:
            return int(wire)
        except ValueError:
            if wire not in self.results:
                ops = self.wires[wire]
                if len(ops) == 1:
                    res = self.get_signal(ops[0])
                else:
                    op = ops[-2]
                    if op == "NOT":
                        res = ~self.get_signal(ops[1]) & 0xffff
                    elif op == "AND":
                        res = self.get_signal(ops[0]) & self.get_signal(ops[2])
                    elif op == "OR":
                        res = self.get_signal(ops[0]) | self.get_signal(ops[2])
                    elif op == "LSHIFT":
                        res = self.get_signal(ops[0]) << self.get_signal(ops[2])
                    elif op == "RSHIFT":
                        res = self.get_signal(ops[0]) >> self.get_signal(ops[2])
                self.results[wire] = res
            return self.results[wire]



def main():
    data = [ line.rstrip("\n") for line in open("input07") ]

    c = Circuit(data)
    res1 = c.get_signal("a")
    print(res1)
    
    c.results.clear()
    c.results["b"] = res1
    res2 = c.get_signal("a")
    print(res2)


if __name__ == "__main__":
    main()

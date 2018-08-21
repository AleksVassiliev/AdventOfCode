class CircularList:
    def __init__(self, lst):
        self.data = lst
        self.size = len(lst)


    def get(self, idx):
        while idx >= self.size:
            idx -= self.size
        return self.data[idx]


    def set(self, idx, value):
        while idx >= self.size:
            idx -= self.size
        self.data[idx] = value


    def max(self):
        return max(self.data)


    def index(self, value):
        return self.data.index(value)



class MemoryCache():
    def __init__(self):
        self.cache = []


    def addState(self, line):
        state = ".".join(str(x) for x in line)
        if state in self.cache:
            self.cache.append(state)
            return False
        self.cache.append(state)
        return True


    def getLoopLength(self):
        value = self.cache[-1]
        return (len(self.cache) - self.cache.index(value) - 1)


class Memory():
    def __init__(self):
        self.mcache = MemoryCache()


    def balanceStep(self, state):
        clist = CircularList(state)

        max_value = clist.max()
        max_index = clist.index(max_value)

        clist.set(max_index, 0)
        while max_value > 0:
            max_index += 1
            value = clist.get(max_index) + 1
            clist.set(max_index, value)
            max_value -= 1

        return clist.data


    def balance(self, state):
        step = 1
        self.mcache.cache.clear()
        self.mcache.addState(state)

        while True:
            state = self.balanceStep(state)
            if self.mcache.addState(state) == False:
                return step
            else:
                step += 1


    def getLoopLength(self):
        return self.mcache.getLoopLength()



def main():
    state = [ 0, 2, 7, 0 ]
    mem = Memory()
    assert(mem.balance(state) == 5)
    assert(mem.getLoopLength() == 4)

    content = [ line.rstrip('\n') for line in open("input06") ]
    data = content[0].split('\t')
    data = [ int(x) for x in data ]
    print(mem.balance(data), mem.getLoopLength())

if __name__ == "__main__":
    main()

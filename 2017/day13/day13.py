firewall = [ "0: 3", "1: 2", "4: 4", "6: 4" ]


def test_partA():
    assert(tripSeverity(firewall) == 24)


def test_partB():
    assert(tripDelay(firewall) == 10)


def tripSeverity(data):
    firewall = Firewall(data)
    return firewall.severity()


def tripDelay(data):
    firewall = Firewall(data)
    return firewall.delay()



class Firewall:
    def __init__(self, data):
        self.layers = {}
        self.size = 0
        self.initialize(data)


    def initialize(self, data):
        for item in data:
            v = item.split(": ")
            layer = int(v[0])
            depth = int(v[1])
            self.layers[layer] = depth
            self.size = layer
        self.size += 1

        
    def checkLayer(self, layer, time):
        if layer in self.layers:
            depth = self.layers[layer]
            offset = time % ((depth - 1) * 2)
            position = 0
            if offset > (depth - 1):
                position = (2 * (depth - 1) - offset)
            else:
                position = offset
            if position == 0:
                return False
        return True


    def severity(self):
        severity = 0
        layer = 0
        for time in range(0, self.size):
            if self.checkLayer(layer, time) == False:
                severity += layer * self.layers[layer]
            layer += 1
        return severity


    def checkTrip(self, delay):
        layer = 0
        for time in range(delay, self.size + delay):
            if self.checkLayer(layer, time) == False:
                return False
            layer += 1
        return True


    def delay(self):
        delay = 0
        while True:
            if self.checkTrip(delay) == True:
                return delay
            delay += 1



def main():
    content = [ line.rstrip('\n') for line in open('input13') ]
    firewall = Firewall(content)
    print(firewall.severity())
    print(firewall.delay())


if __name__ == "__main__":
    main()

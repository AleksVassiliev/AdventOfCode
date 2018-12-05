import re
import collections


class BotList(collections.defaultdict):
    def __missing__(self, key):
        value = Bot(key)
        self[key] = value
        return value

    def __repr__(self):
        text = ''
        for key in self:
            text += str(self[key])
        return text



class Bot:
    def __init__(self, name):
        self.name = name
        self.input = []
        self.outl = None
        self.outh = None


    def __repr__(self):
        return '{}: {} - {} {}\n'.format(self.name, self.input, self.outl, self.outh)



class Pipeline:
    def __init__(self, instr):
        self.bots = BotList(Bot)
        self.output = collections.defaultdict(int)
        self.initialize(instr)


    def initialize(self, instr):
        for line in instr:
            if line.startswith("value"):
                regexp = "value\s(\d+)\sgoes\sto\s(bot\s\d+)"
                value, bot = re.search(regexp, line).groups()
                bot = bot.replace(" ", "_")
                self.bots[bot].input.append(int(value))
            elif line.startswith("bot"):
                regexp = "(bot\s\d+)\sgives\slow\sto\s((bot|output)\s\d+)\sand\shigh\sto\s((bot|output)\s\d+)"
                res = re.search(regexp, line).groups()
                bot = res[0].replace(" ", "_")
                outl = res[1].replace(" ", "_")
                outh = res[3].replace(" ", "_")
                self.bots[bot].outl = outl
                self.bots[bot].outh = outh


    def sendValue(self, key, value):
        if key.startswith("output"):
            self.output[key] = value
        else:
            self.bots[key].input.append(value)


    def findBot(self, value1, value2):
        for key in self.bots:
            bot = self.bots[key]
            while len(bot.input) >= 2:
                a = bot.input.pop(0)
                b = bot.input.pop(0)
                min_val = min(a, b)
                max_val = max(a, b)
                self.sendValue(bot.outl, min_val)
                self.sendValue(bot.outh, max_val)
                if (min_val == value1) and (max_val == value2):
                    return bot.name
        return self.findBot(value1, value2)


    def process(self):
        res = False
        for key in self.bots:
            bot = self.bots[key]
            while len(bot.input) >= 2:
                res = True
                a = bot.input.pop(0)
                b = bot.input.pop(0)
                min_val = min(a, b)
                max_val = max(a, b)
                self.sendValue(bot.outl, min_val)
                self.sendValue(bot.outh, max_val)
        return res


    def checksum(self):
        while True:
            res = self.process()
            if res == False:
                crc = self.output["output_0"] * self.output["output_1"] * self.output["output_2"]
                return crc



def main():
    instr = [ line.rstrip("\n") for line in open("input10") ]

    p = Pipeline(instr)
    bot = p.findBot(17, 61)
    print(bot)
    crc = p.checksum()
    print(crc)


if __name__ == "__main__":
    main()

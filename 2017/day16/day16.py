def test_partA():
    data = [ chr(x) for x in range(ord('a'), ord('e') + 1) ]
    moves = [ 's1', 'x3/4', 'pe/b' ]
    
    p = Programs(data)
    p.setMoves(moves)
    res = p.dance(1)

    assert(res == 'baedc')    


class Programs:
    def __init__(self, data):
        self.programs = data
        self.length = len(self.programs)
        self.moves = []


    def dance(self, count):
        seen = []   
        for i in range(count):
            result = "".join(self.programs)
            if result in seen:
                print(i, len(seen))
                return "".join(seen[count % i])

            seen.append(result)
            for move in self.moves:
                value = move[0]
                if value == 's':
                    self.moveSpin(move[1])
                elif value == 'x':
                    self.moveExchange(move[1], move[2])
                elif value == 'p':
                    self.movePartner(move[1], move[2])
        return "".join(self.programs)


    def setMoves(self, moves):
        for move in moves:
            p0 = move[0]
            p1 = None
            p2 = None
            if p0 == 's':
                p1 = int("".join(move[1:]))
            elif p0 == 'x':
                l = move[1:].split("/")
                p1 = int(l[0])
                p2 = int(l[1])
            elif p0 == 'p':
                p1 = move[1]
                p2 = move[3]
            self.moves.append([p0, p1, p2])


    def moveSpin(self, pos):
        pos = self.length - pos
        self.programs = self.programs[pos:] + self.programs[:pos]
 

    def moveExchange(self, pos0, pos1):     
        self.programs[pos0], self.programs[pos1] = self.programs[pos1], self.programs[pos0]


    def movePartner(self, el0, el1):
        pos0 = self.programs.index(el0)
        pos1 = self.programs.index(el1)
        
        self.programs[pos0], self.programs[pos1] = self.programs[pos1], self.programs[pos0]
               


def main():
    data = [ chr(x) for x in range(ord('a'), ord('p') + 1) ]
    with open("input16", "r") as f:
        moves = f.read().rstrip("\n").split(",")

        p = Programs(data)
        p.setMoves(moves)
        res = p.dance(1)
        print(res)
        
        p = Programs(data)
        p.setMoves(moves)
        res = p.dance(1000000000)
        print(res)
        

if __name__ == "__main__":
    main()

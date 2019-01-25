import re
import collections

class Tree:
    def __init__(self):
        self.root = []
        self.tree = collections.defaultdict(list)
        self.rev_tree = collections.defaultdict(list)
        self.order = []


    def parse(self, lines):
        regexp = '^Step\s([A-Z])\smust\sbe\sfinished\sbefore\sstep\s([A-Z])\scan\sbegin.$'
        for line in lines:
            res = re.search(regexp, line).groups()
            self.tree[res[0]].append(res[1])
            self.rev_tree[res[1]].append(res[0])
        for key in self.tree:
            if key not in self.rev_tree:
                self.root.append(key)


    def traverse(self):
        self.unvisited = []
        self.unvisited += self.root 
        while True:
            leaf = self.getLeaf(self.unvisited)
            if leaf == None:
                break
            self.processLeaf(leaf)


    def getLeaf(self, unvisited):
        unvisited.sort()
        for item in unvisited:
            if self.checkLeaf(item) == True:
                return item
        return None


    def checkLeaf(self, leaf):
        for item in self.rev_tree[leaf]:
            if item not in self.order:
                return False
        return True


    def processLeaf(self, leaf):
        self.unvisited.remove(leaf)
        self.order.append(leaf)
        for item in self.tree[leaf]:
            if item not in self.unvisited:
                self.unvisited.append(item)



def main():
    '''
    content = [ 'Step C must be finished before step A can begin.',
                'Step C must be finished before step F can begin.',
                'Step A must be finished before step B can begin.',
                'Step A must be finished before step D can begin.',
                'Step B must be finished before step E can begin.',
                'Step D must be finished before step E can begin.',
                'Step F must be finished before step E can begin.'
              ]
    '''
    content = [ x.rstrip('\n') for x in open('input07') ]
    
    tree = Tree()
    tree.parse(content)
    tree.traverse()
    print(''.join(tree.order))


if __name__ == '__main__':
    main()

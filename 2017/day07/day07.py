import copy

testTree = [ "pbga (66)",
             "xhth (57)",
             "ebii (61)",
             "havc (66)",
             "ktlj (57)",
             "fwft (72) -> ktlj, cntj, xhth",
             "qoyq (66)",
             "padx (45) -> pbga, havc, qoyq",
             "tknk (41) -> ugml, padx, fwft",
             "jptl (61)",
             "ugml (68) -> gyxo, ebii, jptl",
             "gyxo (61)",
             "cntj (57)"
           ]


def test_partA():
    tree = Tree(testTree)
    assert(tree.root() == "tknk")


def test_partB():
    tree = Tree(testTree)
    assert(tree.balance("tknk") == 60)



class Queue:
    def __init__(self):
        self.queue = []


    def pop(self, lst):
        for item in lst:
            self.queue.append(item)


    def get(self):
        res = self.queue[0]
        del(self.queue[0])
        return res


    def empty(self):
        return (len(self.queue) == 0)



class TreeNode:
    def __init__(self, name, weight, leafs):
        self.name = name
        self.weight = weight
        self.leafs = leafs



class Tree:
    def __init__(self, data):
        self.nodes = {}
        for item in data:
            lst = item.split(" -> ")
            lst0 = lst[0].split(" ")
            n = lst0[0]
            w = int(lst0[1].strip("(").rstrip(")"))
            l = []
            if len(lst) == 2:
                l = lst[1].split(", ")
            self.nodes[n] = TreeNode(n, w, l)
    

    def root(self):
        tree = {}
        for key in self.nodes:
            tree[key] = self.nodes[key].leafs

        while True:
            leafs = set()
            for key in tree:
                if not tree[key]:
                    leafs.add(key)
            for l in leafs:
                tree.pop(l)
            for key in tree:
                data = []
                for l in tree[key]:
                    if l not in leafs:
                        data.append(l)
                tree[key] = copy.copy(data)
            
            root = list(tree)
            if len(root) == 1:
                return root[0]


    def balance(self, node):
        unbalancedBranch = node
        balanceDiff = 0
        while True:
            branch, diff = self.isBalanced(unbalancedBranch)
            if branch is not None:
                unbalancedBranch = branch
                balanceDiff = diff
            else:
                return self.nodes[unbalancedBranch].weight + balanceDiff


    def isBalanced(self, node):
        weights = {}
        branches = self.nodes[node].leafs
        for b in branches:
            weight = self.nodes[b].weight
            
            q = Queue()
            q.pop(self.nodes[b].leafs)
            while q.empty() == False:
                leaf = q.get()
                q.pop(self.nodes[leaf].leafs)
                weight += self.nodes[leaf].weight
            
            if weight in weights:
                weights[weight].append(b)
            else:
                weights[weight] = [ b ]


        branch = None
        diff = 0

        if len(weights) == 2:
            balanced = 0
            unbalanced = 0
            for key in weights:
                if len(weights[key]) == 1:
                    unbalanced = key
                else:
                    balanced = key
            diff = balanced - unbalanced
            branch = weights[unbalanced][0]

        return branch, diff



def main():
    content = [ line.rstrip('\n') for line in open('input07') ]
    tree = Tree(content)
    root = tree.root()
    print(root)
    print(tree.balance(root))

    
if __name__ == "__main__":
    main()

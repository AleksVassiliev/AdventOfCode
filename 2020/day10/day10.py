def calculate_difference(data):
    result = {'1': 0, '3': 1}
    adapters = [ 0 ] + sorted(data)
    for i in range(0, len(adapters)-1):
        adapter1 = adapters[i]
        adapter2 = adapters[i+1]
        diff = adapter2 - adapter1
        if diff == 1:
            result['1'] += 1
        elif diff == 3:
            result['3'] += 1
    return result


class Node:
    def __init__(self, value):
        self.node = value
        self.leaf = []
        self.weight = 1

    def add_leaf(self, node):
        self.leaf.append(node)
        self.weight = 0


class Tree:
    def __init__(self):
        self.root = None
        self.data = None

    def add_subtree(self, value):
        root = Node(value)
        for i in range(1, 4):
            if value + i in self.data:
                node = self.add_subtree(i + value)
                root.add_leaf(node)
        return root

    def generate_tree(self, data):
        self.data = data
        self.root = self.add_subtree(data[0])

    def count_leafs(self, node):
        if not node.leaf:
            return 1
        else:
            result = 0
            for node in node.leaf:
                result += self.count_leafs(node)
            return result

    def count_tree(self):
        return self.count_leafs(self.root)


def calculate_variants(data):
    adapters = [ 0 ] + sorted(data)
    chains = []
    chain = set()
    for e in adapters[:-1]:
        values = [e + x for x in range(1, 4)]
        var = [x for x in values if x in adapters]
        if len(var) == 1:
            if len(chain) > 1:
                chains.append(chain)
                chain = set()
        else:
            chain.add(e)
            chain.update(var)
    if len(chain) > 1:
        chains.append(chain)

    result = 1
    for chain in chains:
        tree = Tree()
        tree.generate_tree(sorted(list(chain)))
        result *= tree.count_tree()
    
    return result
 

def main():
    data = [int(line) for line in open('./input10.txt')]
    result_v1 = calculate_difference(data)
    print(result_v1['1'] * result_v1['3'])
    result_v2 = calculate_variants(data)
    print(result_v2)


if __name__ == '__main__':
    main()

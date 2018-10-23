import copy


def getComponents(data):
    components = []
    for d in data:
        a, b = d.split("/")
        components.append((int(a), int(b)))
    return components


class Node:
    def __init__(self, node, conn, weight, length):
        self.node = node
        self.connection_point = conn
        self.children = []
        self.weight = weight + node[0] + node[1]
        self.length = length + 1


def getRoots(components):
    roots = []
    for c in components:
        if c[0] == 0:
            roots.append(Node(c, c[1], 0, 0))
            components.remove(c)
        elif c[1] == 0:
            roots.append(Node(c, c[0], 0, 0))
            components.remove(c)
    return roots


def getNodes(components, node):
    for c in components:
        if c[0] == node.connection_point:
            new_node = Node(c, c[1], node.weight, node.length)
            node.children.append(new_node)
            new_components = copy.deepcopy(components)
            new_components.remove(c)
            getNodes(new_components, new_node)
        elif c[1] == node.connection_point:
            new_node = Node(c, c[0], node.weight, node.length)
            node.children.append(new_node)
            new_components = copy.deepcopy(components)
            new_components.remove(c)
            getNodes(new_components, new_node)            


def getStrength1(node):
    if not node.children:
        return node.weight
    else:
        res = 0
        for c in node.children:
            s = getStrength1(c)
            if s > res:
                res = s
        return res


def getStrength2(node):
    if not node.children:
        return node.weight, node.length
    else:
        rw = 0
        rl = 0
        for c in node.children:
            w, l = getStrength2(c)
            if l > rl:
                rl = l
                rw = w
            else:
                if l == rl:
                    if w > rw:
                        rw = w
        return rw, rl



def strength(data):
    components = getComponents(data)

    res1 = 0
    res2w = 0
    res2l = 0
    roots = getRoots(components)
    for r in roots:
        getNodes(components, r)
        s1 = getStrength1(r)
        w2, l2 = getStrength2(r)
        if s1 > res1:
            res1 = s1
        if l2 > res2l:
            res2l = l2
            res2w = w2
        elif l2 == res2l:
            if w2 > res2w:
                res2w = w2
    return res1, res2w


def main():
    test_data = [ "0/2", "2/2", "2/3", "3/4", "3/5", "0/1", "10/1", "9/10" ]
    res1, res2 = strength(test_data)
    print(res1, res2)
    
    data = [ line.rstrip("\n") for line in open("input24") ]
    res1, res2 = strength(data)
    print(res1, res2)
    

if __name__ == "__main__":
    main()
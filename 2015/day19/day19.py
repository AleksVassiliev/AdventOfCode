molecule_elem = [ chr(x) for x in range(ord('A'), ord('Z') + 1)]


def molecule2elements(molecule):
    elements = []
    m = molecule[0]
    for c in molecule[1:]:
        if c in molecule_elem:
            elements.append(m)
            m = c
        else:
            m += c
    elements.append(m)
    return elements


def generateMolecules(pattern, replacements):
    res = set()
    for idx, elem in enumerate(pattern):
        if elem in replacements:
            repl = replacements[elem]
            for r in repl:
                mol = pattern[:]
                mol[idx] = r
                res.add("".join(mol))
    return res


def analyze(elements):
    element = 0
    parentless = 0
    term = 0
    for e in elements:
        if e == "Y":
            term += 1
        elif (e == "Rn") or (e == "Ar"):
            parentless += 1
        element += 1
    res = element - parentless - 2 * term - 1
    return res


def main():
    data = [ line.rstrip("\n") for line in open("input19") ]
    
    replacements = {}
    for line in data[:-2]:
        src, dst = line.split(" => ")
        if src in replacements:
            replacements[src].append(dst)
        else:
            replacements[src] = [ dst ]

    pattern = molecule2elements(data[-1])

    res = generateMolecules(pattern, replacements)
    print(len(res))

    res = analyze(pattern)
    print(res)

if __name__ == "__main__":
    main()

def combinations(cont, part_comb=[]):
    res = []
    for idx, c in enumerate(cont):
        ext_part = part_comb[:]
        ext_part.append(c)
        if sum(ext_part) == 150:
            res.append(ext_part)
        elif sum(ext_part) < 1500:
            ext_cont = cont[idx+1:]
            res += combinations(ext_cont, ext_part)
        else:
            pass
    return res


def main():
    containers = [ int(line.rstrip("\n")) for line in open("input17") ]

    comb = combinations(containers)
    print(len(comb))

    amount = []
    for i in range(len(containers)):
        amount.append(0)
    for c in comb:
        amount[len(c)] += 1
    for v in amount:
        if v != 0:
            print(v)
            break



if __name__ == "__main__":
    main()

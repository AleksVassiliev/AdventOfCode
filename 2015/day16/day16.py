checklist = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def check1(aunts):
    for key in aunts:
        res = True
        for val in aunts[key]:
            if aunts[key][val] == checklist[val]:
                res = res & True
            else:
                res = False
        if res == True:
            return key


def check2(aunts):
    for key in aunts:
        res = True
        for val in aunts[key]:
            if (val == "cats") or (val == "trees"):
                if aunts[key][val] > checklist[val]:
                    res = res & True
                else:
                    res = False
            elif (val == "pomeranians") or (val == "goldfish"):
                if aunts[key][val] < checklist[val]:
                    res = res & True
                else:
                    res = False
            else:
                if aunts[key][val] == checklist[val]:
                    res = res & True
                else:
                    res = False
        if res == True:
            return key


def main():
    aunts = {}
    data = [ line.rstrip("\n") for line in open("input16") ]
    for item in data:
        lst = item.split(": ")
        name = lst[0]
        values = " ".join(lst[1:]).split(", ")
        aunts[name] = {}
        for val in values:
            key, v = val.split(" ")
            aunts[name][key] = int(v)

    res = check1(aunts)
    print(res)

    res = check2(aunts)
    print(res)


if __name__ == "__main__":
    main()

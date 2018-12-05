import re
import string


def reaction(formula):
    polymer = ""
    i = 0
    while i < len(formula) - 1:
        cl = ord(formula[i])
        cr = ord(formula[i+1])
        if abs(cl - cr) != 32:
            polymer += formula[i]
            i += 1
        else:
            i += 2
    if i == len(formula) - 1:
        polymer += formula[i]
    return polymer


def makePolymer1(polymer):
    ini_len = len(polymer)
    pol_len = 0
    while True:
        polymer = reaction(polymer)
        pol_len = len(polymer)
        if pol_len == ini_len:
            return len(polymer)
        ini_len = pol_len


def makePolymer2(formula):
    az = string.ascii_lowercase
    AZ = string.ascii_uppercase

    min_size = len(formula)
    for i in range(len(az)):
        chars = '{}{}'.format(az[i], AZ[i])
        rx = '[' + re.escape(chars) + ']'
        polymer = re.sub(rx, '', formula)
        if len(polymer) < len(formula):
            res = makePolymer1(polymer)
            min_size = min(res, min_size)
    return min_size


def main():    
    with open("input05") as f:
        polymer = f.read().rstrip("\n")    

        res1 = makePolymer1(polymer)
        print(res1)

        res2 = makePolymer2(polymer)
        print(res2)
    

if __name__ == "__main__":
    main()

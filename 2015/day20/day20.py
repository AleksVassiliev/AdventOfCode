import math

def get_factors(x):
    factors = set()
    factors.add(1)
    factors.add(x)
    for i in range(2, math.ceil(math.sqrt(x)) + 1): 
        if x % i == 0: 
            factors.add(i)
            factors.add(x//i)
    return factors


def countPresentsA(max_presents):
    house = 0
    while True:
        house += 1    
        elves = get_factors(house)
        presents = 0
        for e in elves:
            presents += e * 10
        if presents >= max_presents:
            return house


def countPresentsB(max_presents):
    house = 0
    while True:
        house += 1    
        elves = get_factors(house)
        presents = 0
        for e in elves:
            if (e * 50) > house:
                presents += e * 11
        if presents >= max_presents:
            return house


def main():
    presents = 34000000

    res = countPresentsA(presents)
    print(res)

    res = countPresentsB(presents)
    print(res)


if __name__ == "__main__":
    main()

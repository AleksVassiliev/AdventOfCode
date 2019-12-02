import math


def part1(data):
    total_fuel = 0
    for value in data:
        mass = math.floor(value/3) - 2
        total_fuel += mass
    return total_fuel


def part2(data):
    total_fuel = 0
    for value in data:
        mass = math.floor(value/3) - 2
        total_fuel += mass
        while mass > 0:
            mass = math.floor(mass/3) - 2
            if mass > 0:
                total_fuel += mass
    return total_fuel


def main():
    data = [ int(line.rstrip('\n')) for line in open('input01') ]

    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()

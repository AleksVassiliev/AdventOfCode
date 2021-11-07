from collections import defaultdict


def get_spoken_number(num, numbers):
    if num in numbers:
        if len(numbers[num]) > 1:
            return numbers[num][-1] - numbers[num][-2]
    return 0
    

def get_number(numbers, turns):
    nums = defaultdict(list)
    for turn, num in enumerate(numbers):
        nums[num].append(turn + 1)
    turn = len(numbers)
    spoken_number = numbers[-1]
    while turn < turns:
        turn += 1
        last_number = spoken_number
        spoken_number = get_spoken_number(last_number, nums)
        nums[spoken_number].append(turn)
    return spoken_number


def main():
    with open('input15.txt') as fi:
        numbers = fi.readline()
        data = [int(x) for x in numbers.split(',')]
    result_v1 = get_number(data, 2020)
    print(result_v1)
    result_v2 = get_number(data, 30000000)
    print(result_v2)


if __name__ == '__main__':
    main()

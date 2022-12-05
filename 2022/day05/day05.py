import re

def parse_input(data):
    stack_src = []
    moves = []
    to_stack = True
    for line in data:
        if line == '':
            to_stack = False
        else:
            if to_stack:
                stack_src.append(line)
            else:
                moves.append(line)
    stack_num = 0
    for item in stack_src[-1].split(" "):
        if item != '':
            stack_num += 1
    stack = []
    for _ in range(stack_num):
        stack.append([])
    for line in stack_src[:-1]:
        for i in range(0, stack_num):
            if line[4*i+1] != ' ':
                stack[i].append(line[4*i+1])
    return stack, moves


def rearrange_v1(data):
    stack, moves = parse_input(data)
    for line in moves:
        (num, src, dst) = [int(x) for x in re.findall('[0-9]+', line)]
        for _ in range(num):
            stack[dst - 1].insert(0, stack[src - 1].pop(0))
    res = ''
    for item in stack:
        res += item[0]
    return res        


def rearrange_v2(data):
    stack, moves = parse_input(data)
    for line in moves:
        (num, src, dst) = [int(x) for x in re.findall('[0-9]+', line)]
        lst = []
        for _ in range(num):
            lst.append(stack[src - 1].pop(0))
        stack[dst - 1] = lst + stack[dst - 1]
    res = ''
    for item in stack:
        res += item[0]
    return res        


def main():
    data = [line.strip('\n') for line in open('./input.txt')]
    result_v1 = rearrange_v1(data)
    print(result_v1)
    result_v2 = rearrange_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

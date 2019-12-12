def process(data, input_param):
    output_param = None
    pc = 0
    while data[pc] != 99:
        opcode = data[pc] % 100
        mode1 = data[pc] // 100 % 10
        mode2 = data[pc] // 1000 % 10
        mode3 = data[pc] // 10000 % 10
        if opcode == 1:
            value1 = data[pc+1]
            value2 = data[pc+2]
            res = data[pc+3]
            data[res] = (value1 if mode1 == 1 else data[value1]) + (value2 if mode2 == 1 else data[value2])
            pc += 4
        elif opcode == 2:
            value1 = data[pc+1]
            value2 = data[pc+2]
            res = data[pc+3]
            data[res] = (value1 if mode1 == 1 else data[value1]) * (value2 if mode2 == 1 else data[value2])
            pc += 4
        elif opcode == 3:
            res = data[pc+1]
            data[res] = input_param
            pc += 2
        elif opcode == 4:
            res = data[pc+1]
            output_param = res if mode1 == 1 else data[res]
            pc += 2
        elif opcode == 5:
            param1 = data[pc+1]
            param2 = data[pc+2]
            value = param1 if mode1 == 1 else data[param1]
            if value != 0:
                pc = param2 if mode2 == 1 else data[param2]
            else:
                pc += 3
        elif opcode == 6:
            param1 = data[pc+1]
            param2 = data[pc+2]
            value = param1 if mode1 == 1 else data[param1]
            if value == 0:
                pc = param2 if mode2 == 1 else data[param2]
            else:
                pc += 3
        elif opcode == 7:
            param1 = data[pc+1]
            param2 = data[pc+2]
            param3 = data[pc+3]
            value1 = param1 if mode1 == 1 else data[param1]
            value2 = param2 if mode2 == 1 else data[param2]
            if value1 < value2:
                data[param3] = 1
            else:
                data[param3] = 0
            pc += 4
        elif opcode == 8:
            param1 = data[pc+1]
            param2 = data[pc+2]
            param3 = data[pc+3]
            value1 = param1 if mode1 == 1 else data[param1]
            value2 = param2 if mode2 == 1 else data[param2]
            if value1 == value2:
                data[param3] = 1
            else:
                data[param3] = 0
            pc += 4

    return output_param


def main():
    content = open('input05').read().rstrip('\n').split(',')
    
    data = [ int(x) for x in content ]
    print(process(data, 1))

    data = [ int(x) for x in content ]
    print(process(data, 5))


if __name__ == '__main__':
    main()

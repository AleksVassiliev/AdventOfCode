from collections import defaultdict


def simulate_v1(data):
    counter = 0
    for idx in range(len(data)):
        if data[idx] > 0:
            data[idx] -= 1
        else:
            data[idx] = 6
            counter += 1
    for _ in range(counter):
        data.append(8)


def simulate_v2(data):
    data_prev = data.copy()
    data[0] = data_prev[1]
    data[1] = data_prev[2]
    data[2] = data_prev[3]
    data[3] = data_prev[4]
    data[4] = data_prev[5]
    data[5] = data_prev[6]
    data[6] = data_prev[7] + data_prev[0]
    data[7] = data_prev[8]
    data[8] = data_prev[0]
    

def calculate_v1(data):
    data = data.copy()
    for _ in range(80):
        simulate_v1(data)
    return len(data)


def calculate_v2(data):
    fishes = defaultdict(int)
    for item in data:
        fishes[item] += 1
    for _ in range(256):
        simulate_v2(fishes)
    result = 0
    for key in fishes:
        result += fishes[key]
    return result


def main():
    data = [int(x) for x in open('./input06.txt').readline().split(',')]
    result_v1 = calculate_v1(data)
    print(result_v1)
    result_v2 = calculate_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

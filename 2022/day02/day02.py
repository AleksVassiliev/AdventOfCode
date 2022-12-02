score_shape = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

matrix_v1 = {
    'A': { 'X': 3, 'Y': 6, 'Z': 0 },
    'B': { 'X': 0, 'Y': 3, 'Z': 6 },
    'C': { 'X': 6, 'Y': 0, 'Z': 3 }
}

matrix_v2 = {
    'A': ['Z', 'X', 'Y'], 
    'B': ['X', 'Y', 'Z'],
    'C': ['Y', 'Z', 'X']
}

score_outcome = {
    'X': 0,
    'Y': 3,
    'Z': 6
}


def calculate_score_v1(data):
    score = 0
    for item in data:
        opp, you = item.split(' ')
        score += score_shape[you] + matrix_v1[opp][you]
    return score


def calculate_score_v2(data):
    score = 0
    for item in data:
        opp, res = item.split(' ')
        you = matrix_v2[opp][score_outcome[res]//3]
        score += score_shape[you] + score_outcome[res]
    return score



def main():
    data = [line.strip() for line in open('./input.txt')]
    result_v1 = calculate_score_v1(data)
    print(result_v1)
    result_v2 = calculate_score_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

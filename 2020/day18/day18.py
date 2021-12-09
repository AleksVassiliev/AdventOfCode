import operator


def evaluate(expression, ops):
    OPERATORS = ops

    def parse(expression):
        number = ''
        for s in expression:
            if s in '1234567890.':
                number += s
            elif number:
                yield int(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield int(number)

    def sorting(tokens):
        stack = []
        for token in tokens:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(tokens):
        stack = []
        for token in tokens:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(sorting(parse(expression)))


def evaluate_v1(expression):
    ops = {'+': (1, operator.add), '*': (1, operator.mul)}
    return evaluate(expression, ops)


def evaluate_v2(expression):
    ops = {'+': (2, operator.add), '*': (1, operator.mul)}
    return evaluate(expression, ops)


def calculate_v1(data):
    res = 0
    for line in data:
        res += evaluate_v1(line)
    return res


def calculate_v2(data):
    res = 0
    for line in data:
        res += evaluate_v2(line)
    return res


def main():
    data = [line.strip() for line in open('input18.txt')]
    result_v1 = calculate_v1(data)
    print(result_v1)
    result_v2 = calculate_v2(data)
    print(result_v2)


if __name__ == '__main__':
    main()

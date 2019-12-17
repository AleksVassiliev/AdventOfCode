import math
import collections

'''
Q1  T   Q0
 L  P   R
Q2  B   Q3
'''

def length(x0, y0, x1, y1):
    return math.sqrt(math.pow(x0-x1, 2) + math.pow(y0-y1, 2))

def angle(l1, l2):
    return round(min(l1, l2)/max(l1, l2), 4)

def quadrant(x0, y0, x1, y1):
    if (x0 == x1) and (y0 < y1):
        return 'T'
    if (x0 == x1) and (y0 > y1):
        return 'B'
    if (x0 < x1) and (y0 == y1):
        return 'R'
    if (x0 > x1) and (y0 == y1):
        return 'L'
    if (x0 < x1) and (y0 < y1):
        return 'Q0'
    if (x0 < x1) and (y0 > y1):
        return 'Q3'
    if (x0 > x1) and (y0 < y1):
        return 'Q1'
    if (x0 > x1) and (y0 > y1):
        return 'Q2'

def count_asteroids(data, x0, y0):
    result_line = collections.defaultdict(int)
    result_sector = collections.defaultdict(set)
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            if cell == '#':
                q = quadrant(x0, y0, x, y)
                if q in ['T', 'B', 'L', 'R']:
                    result_line[q] = length(x0, y0, x, y)
                elif q in ['Q0', 'Q1', 'Q2', 'Q3']:
                    l1 = length(x0, y0, x, y)
                    l2 = length(x0, y0, x, y0)
                    result_sector[q].add(angle(l1, l2))

    result = 0
    for k in result_line:
        result += 1
    for k in result_sector:
        result += len(result_sector[k])

    return result


def main():
    data = [ x.rstrip('\n') for x in open('input10') ]

    result = 0
    for j, line in enumerate(data):
        for i, cell in enumerate(line):
            if cell == '#':
                res = count_asteroids(data, i, j)
                result = max(res, result)
    print(result)

    
if __name__ == '__main__':
    main()

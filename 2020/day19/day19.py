def get_string(key, rules):
    if type(rules[key]) != list:
        return [rules[key]]
    return rules[key]



def analyze(data):
    rules = {}
    for line in data:
        key, value = line.split(': ')
        value = value.strip('"')
        if '|' in value:
            value = value.split(' | ')
        rules[key] = value
    
    cur_str = rules['0'].split()
    next_str = ''
    for ch in cur_str:
        c = rules[ch]
        if type(c) != list:
            next_str += f' {c}'
        else:
            next_str = [next_str] * len(c)
            for i in range(len(c)):
                next_str[i] += f' {c[i]}'
    print(next_str)

    res = []
    for line in next_str:
        print(line)
        new_line = ''
        for ch in line.split():
            if ch in rules:
                if type(c) != list:
                    new_line += f' {c}'
                else:
                    new_line = [new_line] * len(c)
                    for i in range(len(c)):
                        new_line[i] += f' {c[i]}'
            else:
                new_line += f' {ch}'

    res.append(new_line)
    print(res)

        




def main():
    data = [line.strip() for line in open('input19.txt')]
    #result_v1 = calculate_v1(data)
    #print(result_v1)
    #result_v2 = calculate_v2(data)
    #print(result_v2)


if __name__ == '__main__':
    main()

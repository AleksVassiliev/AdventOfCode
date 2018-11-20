import json


def parse_list(data, prop):
    res = 0
    for item in data:
        if type(item) is list:
            res += parse_list(item, prop)
        elif type(item) is dict:
            res += parse_dict(item, prop)
        elif type(item) is int:
            res += item
        else:
            pass
    return res


def parse_dict(data, prop):
    res = 0
    for key in data:
        if type(data[key]) is list:
            res += parse_list(data[key], prop)
        elif type(data[key]) is dict:
            res += parse_dict(data[key], prop)
        elif type(data[key]) is int:
            res += data[key]
        elif type(data[key]) is str:
            if data[key] == prop:
                return 0
        else:
            pass
    return res


def parse_json(data, prop=None):
    return parse_dict(data, prop)
        

def main():
    content = json.load(open("input12"))
    res1 = parse_json(content)
    print(res1)
    res2 = parse_json(content, "red")
    print(res2)


if __name__ == "__main__":
    main()
 
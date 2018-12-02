import re


def checkSubstrTLS(substr):
    if substr[0] != substr[1]:
        if (substr[0] == substr[3]) and (substr[1] == substr[2]):
            return True
    return False


def isValidStringTLS(text):
    all_parts = re.findall('([a-z]+)', text)
    negative = re.findall('\[([a-z]*)\]', text)
    positive = [ item for item in all_parts if item not in negative ]

    for item in negative:
        for i in range(0, len(item)-3):
            if checkSubstrTLS(item[i:i+4]):
                return False

    for item in positive:
        for i in range(0, len(item)-3):
            if checkSubstrTLS(item[i:i+4]):
                return True

    return False


def substrSSL_BAB(substr):
    if (substr[0] == substr[2]) and (substr[0] != substr[1]):
        return substr
    return None


def isValidStringSSL(text):
    all_parts = re.findall('([a-z]+)', text)
    negative = re.findall('\[([a-z]*)\]', text)
    positive = [ item for item in all_parts if item not in negative ]

    bab_list = []
    for item in negative:
        for i in range(0, len(item)-2):
            res = substrSSL_BAB(item[i:i+3])
            if res is not None:
                bab_list.append(res)

    for bab_item in bab_list:
        aba = ""
        aba += bab_item[1]
        aba += bab_item[0]
        aba += bab_item[1]
        for item in positive:
            if item.find(aba) != -1:
                return True

    return False
        

def main():
    data = [ line.rstrip("\n") for line in open("input07") ]

    tls = 0
    ssl = 0
    for item in data:
        if isValidStringTLS(item):
            tls += 1
        if isValidStringSSL(item):
            ssl += 1
    print(tls)
    print(ssl)


if __name__ == "__main__":
    main()

def decompress(text):
    dtext = ""
    marker = ""
    flag = False
    i = 0
    while i < len(text):
        if text[i] == "(":
            flag = True
        elif text[i] == ')':
            chrs, rep = map(int, marker.split("x"))
            new_text = text[i+1:i+chrs+1] 
            for r in range(rep):
                dtext += new_text
            i += chrs
            flag = False
            marker = ""
        else:
            if flag:
                marker += text[i]
            else:
                dtext += text[i]
        i += 1
    return dtext


def decompress2(text):
    dtext = 0
    marker = ""
    flag = False
    i = 0
    while i < len(text):
        if text[i] == "(":
            flag = True
        elif text[i] == ')':
            chrs, rep = map(int, marker.split("x"))
            new_text = text[i+1:i+chrs+1]
            new_text_len = decompress2(new_text)
            dtext += (new_text_len * rep)
            i += chrs
            flag = False
            marker = ""
        else:
            if flag:
                marker += text[i]
            else:
                dtext += 1
        i += 1
    return dtext


def main():
    with open("input09") as f:
        content = f.read().rstrip("\n")
        dec1 = decompress(content)
        dec2 = decompress2(content)
        print(len(dec1), dec2)
    

if __name__ == "__main__":
    main()

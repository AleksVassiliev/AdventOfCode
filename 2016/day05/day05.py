import hashlib


def hash5a(data, idx):
    while True:
        m = hashlib.md5()
        input_string = "{}{}".format(data, idx)
        m.update(input_string.encode())
        hash_string = m.hexdigest()
        if hash_string.startswith("00000"):
            return hash_string[5], (idx+1)
        idx += 1


def hash5b(data, idx):
    while True:
        m = hashlib.md5()
        input_string = "{}{}".format(data, idx)
        m.update(input_string.encode())
        hash_string = m.hexdigest()
        if hash_string.startswith("00000"):
            return hash_string[5], hash_string[6], (idx+1)
        idx += 1



def main():
    doorId = "ojvtpuvg"
    
    password = ""
    idx = 0
    for i in range(8):
        letter, idx = hash5a(doorId, idx)
        password += letter
    print(password)
    
    password = [ None ] * 8
    idx = 0
    flag = True
    while flag:
        pos, letter, idx = hash5b(doorId, idx)
        try:
            pos = int(pos)
            if pos < 8:
                if password[pos] == None:
                    password[pos] = letter
            flag = False
            for e in password:
                if e == None:
                    flag = True
                    break
        except ValueError:
            pass
    print("".join(password))



if __name__ == "__main__":
    main()

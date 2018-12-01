'''
pip3 install sortedcontainers
'''

import sortedcontainers

def main():
    content = [ int(line.rstrip("\n")) for line in open("input01") ]

    freq = 0
    for val in content:
        freq += val
    print(freq)

    freq = 0
    freqlist = sortedcontainers.SortedList()
    freqlist.add(freq)
    while True:
        for val in content:
            freq += val
            if freq in freqlist:
                print(freq)
                return
            freqlist.add(freq)


if __name__ == "__main__":
    main()

class Data:
    def __init__(self, data):
        self.ranges = {}
        self.my_ticket = []
        self.tickets = []
        self.parse(data)

    def parse_ranges(self, line):
        title, ranges = line.split(': ')
        self.ranges[title] = set()
        for item in ranges.split(' or '):
            val_min, val_max = item.split('-')
            self.ranges[title].update(range(int(val_min), int(val_max) + 1))

    @staticmethod
    def line_to_list(line):
        return [int(x) for x in line.split(',')]

    def parse_ticket(self, line):
        self.my_ticket = self.line_to_list(line)

    def parse_tickets(self, line):
        self.tickets.append(self.line_to_list(line))

    def parse(self, data):
        func = self.parse_ranges
        for line in data:
            if line == '':
                continue
            if line == 'your ticket:':
                func = self.parse_ticket
                continue
            if line == 'nearby tickets:':
                func = self.parse_tickets
                continue
            func(line)

    @property
    def overall_range(self):
        result = set()
        for key in self.ranges:
            result.update(self.ranges[key])
        return result


def check_ticket(ticket, overall_range):
    res = 0
    for value in ticket:
        if value not in overall_range:
            res += value
    return res


def check_tickets(data):
    data = Data(data)
    res = 0
    overall_range = data.overall_range
    for ticket in data.tickets:
        res += check_ticket(ticket, overall_range)
    return res


def reduce_variants(variants):
    tickets_count = len(variants)
    variants_count = len(variants[0])
    result = []
    for item in variants:
        result.append(item[0])
    for i in range(variants_count):
        for j in range(tickets_count):
            if result[i]:
                if variants[j][i]:
                    result[i] = list(set(result[i]) & set(variants[j][i]))
            else:
                result[i] = variants[j][i]
    for idx, item in enumerate(result):
        if item and len(item) == 1:
            return idx, item[0]
    return None, None


def decode_ticket(data):
    data = Data(data)
    result = [None] * len(data.tickets[0])
    tickets = []
    overall_range = data.overall_range
    for ticket in data.tickets:
        if check_ticket(ticket, overall_range) == 0:
            tickets.append(ticket)
    all_variants = []
    for ticket in tickets:
        variants = []
        for value in ticket:
            variant = []
            for key in data.ranges:
                if value in data.ranges[key]:
                    variant.append(key)
            variants.append(variant)
        all_variants.append(variants)
    while None in result:
        idx, key = reduce_variants(all_variants)
        result[idx] = key
        for variants in all_variants:
            variants[idx] = None
            for variant in variants:
                if variant:
                    variant.remove(key)
    d = {}
    for idx, item in enumerate(result):
        d[item] = data.my_ticket[idx]
    return d


def multiply_values(data):
    res = 1
    for key in data:
        if key.startswith('departure'):
            res *= data[key]
    return res


def main():
    data = [line.strip() for line in open('input16.txt')]
    result_v1 = check_tickets(data)
    print(result_v1)
    ticket = decode_ticket(data)
    result_v2 = multiply_values(ticket)
    print(result_v2)


if __name__ == '__main__':
    main()

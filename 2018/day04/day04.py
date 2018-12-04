import re
import datetime


def getDate(text):
    regexp = "\[(.+)\].+"
    dt = re.search(regexp, text).groups()[0]
    date = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M")
    if date.hour != 0:
        date = date + datetime.timedelta(days=1)
        date = date.replace(hour=0, minute=0)
    return date


def getGuard(text):
    regexp = "\[.+\]\sGuard\s#(\d+).+"
    guard = re.search(regexp, text).groups()[0]
    return guard


def guardsSchedule(content):
    falls = 0
    wakes = 0
    guard = None
    timeline = [0] * 60
    guards = {}
    for item in content:
        date = getDate(item)
        if item.find("Guard #") != -1:
            if guard is not None:
                key = str(guard)
                if key not in guards:
                    guards[key] = []
                guards[key].append(timeline.copy())
            guard = getGuard(item)
            timeline = [0] * 60
        elif item.find("falls asleep") != -1:
            falls = date.minute
        elif item.find("wakes up") != -1:
            wakes = date.minute
            for i in range(falls, wakes):
                timeline[i] = 1
    key = str(guard)
    if key not in guards:
        guards[key] = []
    guards[key].append(timeline.copy())
    return guards


def strategy1(guards):
    guard = None
    max_guard_sleep = 0
    max_value = 0
    for key in guards:
        res = [0] * 60
        for line in guards[key]:
            for i in range(60):
                res[i] += line[i]

        guard_sleep = sum(res)        
        if guard_sleep > max_guard_sleep:
            guard = key
            max_guard_sleep = guard_sleep
            max_value = res.index(max(res))
    res = int(guard) * max_value
    return res


def strategy2(guards):
    guard = None
    max_guard_sleep = 0
    max_value = 0
    for key in guards:
        res = [0] * 60
        for line in guards[key]:
            for i in range(60):
                res[i] += line[i]

        guard_sleep = max(res)
        if guard_sleep > max_guard_sleep:
            guard = key
            max_guard_sleep = guard_sleep
            max_value = res.index(max(res))
    res = int(guard) * max_value
    return res



def main():
    content = [ line.rstrip("\n") for line in open("input04") ]
    content.sort()
    
    guards = guardsSchedule(content)
    print(strategy1(guards))
    print(strategy2(guards))


if __name__ == "__main__":
    main()

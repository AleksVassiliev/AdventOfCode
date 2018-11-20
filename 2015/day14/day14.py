def run_a(reindeer):
    res = 0
    for item in reindeer:
        (speed, speed_time, rest_time) = reindeer[item]
        distance = 0
        cur_time = 0
        max_time = 2503
        while cur_time < max_time:
            if cur_time + speed_time > max_time:
                speed_time = max_time - cur_time
            distance += speed * speed_time
            cur_time += (speed_time + rest_time)
        res = max(res, distance)
    return res


def run_b(reindeer):
    results = {}
    distance = {}
    for name in reindeer:
        results[name] = 0
        distance[name] = 0

    for cur_time in range(2503):
        name = None
        for item in reindeer:
            (speed, speed_time, rest_time) = reindeer[item]
            cur_sec = cur_time % (speed_time + rest_time)
            if cur_sec < speed_time:
                distance[item] += speed
        dist = 0
        for item in distance:
            dist = max(dist, distance[item])
        for item in distance:
            if distance[item] == dist:
                results[item] += 1

    res = 0
    for item in results:
        res = max(res, results[item])
    return res


def main():
    content = [ line.rstrip("\n") for line in open("input14") ]

    reindeer = {}
    for line in content:
        lst = line.split(" ")
        name = lst[0]
        speed = int(lst[3])
        speed_time = int(lst[6])
        rest_time = int(lst[-2])
        reindeer[name] = (speed, speed_time, rest_time)

    res = run_a(reindeer)
    print(res)

    res = run_b(reindeer)
    print(res)

if __name__ == "__main__":
    main()

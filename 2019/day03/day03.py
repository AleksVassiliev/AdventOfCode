import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __repr__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def distance(self):
        return abs(self.x) + abs(self.y)


class Segment:
    def __init__(self, point, path):
        self.start = Point(point.x, point.y)
        self.end = Point(point.x, point.y)
        if path[0] == 'R':
            self.direction = 'horizontal'
            self.end.x += int(path[1:])
        elif path[0] == 'L':
            self.direction = 'horizontal'
            self.end.x -= int(path[1:])
        elif path[0] == 'U':
            self.direction = 'vertical'
            self.end.y += int(path[1:])
        elif path[0] == 'D':
            self.direction = 'vertical'
            self.end.y -= int(path[1:])

    def __str__(self):
        return '{p0} - {p1}'.format(p0=self.start, p1=self.end)

    def endpoint(self):
        return Point(self.end.x, self.end.y)

    def contains(self, point):
        x0 = min(self.start.x, self.end.x)
        x1 = max(self.start.x, self.end.x)
        y0 = min(self.start.y, self.end.y)
        y1 = max(self.start.y, self.end.y)
        if (x0 <= point.x <= x1) and (y0 <= point.y <= y1):
            return True
        return False

    def intersect(self, other):
        if self.direction != other.direction:
            if self.direction == 'vertical':
                point = Point(self.start.x, other.start.y)
            else:
                point = Point(other.start.x, self.start.y)
            if self.contains(point) and other.contains(point):
                if point.x != 0 and point.y != 0:
                    return point
        return None

    def length(self, point=None):
        if self.direction == 'horizontal':
            if point is None:
                return abs(self.end.x - self.start.x)
            else:
                return abs(point.x - self.start.x)
        else:
            if point is None:
                return abs(self.end.y - self.start.y)
            else:
                return abs(point.y - self.start.y)


class Wire:
    def __init__(self, data):
        self.segments = []
        items = data.split(',')
        point = Point(0, 0)
        for path in items:
            seg = Segment(point, path)
            self.segments.append(seg)
            point = seg.endpoint()

    def distance(self, point):
        distance = 0
        for seg in self.segments:
            if seg.contains(point):
                distance += seg.length(point)
                return distance
            else:
                distance += seg.length()
        return distance
        

def main():
    data = [ line.rstrip('\n') for line in open('input03') ]
    wireA = Wire(data[0])
    wireB = Wire(data[1])

    intersections = []
    for w0 in wireA.segments:
        for w1 in wireB.segments:
            res = w0.intersect(w1)
            if res is not None:
                intersections.append(res)

    distance = sys.maxsize
    for p in intersections:
        distance = min(distance, p.distance())
    print(distance)

    distance = sys.maxsize
    for p in intersections:
        distance = min(distance, wireA.distance(p) + wireB.distance(p))
    print(distance)


if __name__ == '__main__':
    main()

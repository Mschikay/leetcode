class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d

            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)


import heapq


class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.pq = [(self.dist(-1, N), -1, N)]

    # length of the interval (x, y)
    def dist(self, x, y):
        if -1 == x:
            return -1 * y
        elif self.N == y:
            return -1 * (self.N - 1 - x)
        return -1 * (abs(y - x) // 2)

    def seat(self) -> int:
        _, x, y = heapq.heappop(self.pq)
        if -1 == x:
            seat = 0
        elif self.N == y:
            seat = self.N - 1
        else:
            seat = (x + y) // 2
        heapq.heappush(self.pq, (self.dist(x, seat), x, seat))
        heapq.heappush(self.pq, (self.dist(seat, y), seat, y))
        return seat

    def leave(self, p: int) -> None:
        left, right = None, None
        for interval in self.pq:
            if p == interval[1]:
                right = interval
            if interval[2] == p:
                left = interval
            if left and right:
                break
        self.pq.remove(right)
        self.pq.remove(left)
        heapq.heapify(self.pq)  # important! re-heapify after deletion
        heapq.heappush(self.pq, (self.dist(left[1], right[2]), left[1], right[2]))
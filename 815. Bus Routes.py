class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stop2bus = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop2bus[stop].add(i)

        visited_bus = {}
        visited_stop = {S: True}
        deque = collections.deque([(S, 0)])
        while deque:
            stop, step = deque.popleft()
            if stop == T:
                return step
            for bus in stop2bus[stop]:
                if bus not in visited_bus:
                    visited_bus[bus] = True
                    for stop in routes[bus]:
                        if stop not in visited_stop:
                            visited_stop[stop] = True
                            deque.append((stop, step + 1))
        return -1
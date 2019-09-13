from heapq import *
from collections import defaultdict

'''
same entering, process the highest first
same leaving, process the lowest first
leave and enter together, process enter first
refer to https://www.youtube.com/watch?v=GSBLe8cKu0s
'''


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        num = defaultdict(lambda: 0)
        for l, r, h in buildings:
            events.append([l, 1, h])
            events.append([r, -1, h])
            num[l] += 1
            num[r] += 1
        events.sort()
        h = []
        heapify(h)
        ans = []
        pre = float("-inf")
        for i, status, height in events:
            num[i] -= 1
            if status == 1:
                heappush(h, -height)
            else:
                h.remove(-height)
                heapify(h)
            curr = -h[0] if h else 0
            if curr != pre and not num[i]:
                pre = curr
                ans.append([i, curr])
        return ans

    import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points_of_interest = []
        for i, building in enumerate(buildings):
            left, right, height = building
            points_of_interest.append((left, height, i))  # building start
            points_of_interest.append((right, 0, i))  # building end -- height == 0

        # if two start at the same time, tallest should be first
        # if two end at the same time, smallest should be first
        # if one starts and one ends at the same time, former goes first
        #
        # start > end; then order by height descending, which means need to negate
        points_of_interest = sorted(points_of_interest, key=lambda x: (x[0], -x[1]))

        heap = [(0, float('inf'))]
        prev_max_height = 0
        result = []

        for point in points_of_interest:
            position, height, index = point
            if height > 0:
                # building starts
                building = buildings[index]
                _, end, _ = building
                heapq.heappush(heap, (-height, end))
            else:
                # building ends
                while heap[0][1] <= position:
                    heapq.heappop(heap)

            curr_max_height = -heap[0][0]
            if curr_max_height != prev_max_height:
                result.append([position, curr_max_height])
                prev_max_height = curr_max_height

        return result


from heapq import *
from collections import defaultdict


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append([l, h, i])
            events.append([r, 0, i])
            num[l] += 1
            num[r] += 1

        def lt(a, b):
            i_a, status_a, ib_a, i_b, status_b, ib_b = a, b
            if i_a < i_b:
                return -1
            elif i_a == i_b:
                if status_a and status_b:
                    if h_a > h_b:
                        return -1
                    else:
                        return 1
                elif not status_a and not status_b:
                    if building[ib_a][-1] < building[ib_b][-1]:
                        return -1
                    else:
                        return 1
                else:
                    if status_a:
                        return -1
                    else:
                        return 1
            else:
                return 1

        events = sorted(events, lt)
        h = []
        heapify(h)
        ans = []
        pre = float("-inf")
        for i, height index in events:
            if height:
                end = building[index][1]
                heappush(h, (-height, end))
                curr = -h[0]
            else:
                while h[0][1] < i:
                    heappop(h)
                curr = -min(h) if h else 0
            if curr != pre:
                pre = curr
                ans.append([i, curr])
        return ans


